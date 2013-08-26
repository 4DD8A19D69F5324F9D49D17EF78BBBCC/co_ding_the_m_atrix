from vec import Vec
from GF2 import one

from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod
from random import shuffle,randint
from matutil import mat2rowdict

import echelon

## Task 1
def int2GF2(i):
    '''
    Returns one if i is odd, 0 otherwise.

    Input:
        - i: an int
    Output:
        - one if i is congruent to 1 mod 2
        - 0   if i is congruent to 0 mod 2
    Examples:
        >>> int2GF2(3)
        one
        >>> int2GF2(100)
        0
    '''
    if i % 2 == 0:
        return 0
    else:
        return one

## Task 2
def make_Vec(primeset, factors):
    '''
    Input:
        - primeset: a set of primes
        - factors: a list of factors [(p_1,a_1), ..., (p_n, a_n)]
                   with p_i in primeset
    Output:
        - a vector v over GF(2) with domain primeset
          such that v[p_i] = int2GF2(a_i) for all i
    Example:
        >>> make_Vec({2,3,11}, [(2,3), (3,2)]) == Vec({2,3,11},{2:one})
        True
    '''

    return Vec(primeset, {a: int2GF2(b) for a, b in factors})

## Task 3
def find_candidates(N, primeset):
    '''
    Input:
        - N: an int to factor
        - primeset: a set of primes

    Output:
        - a list [roots, rowlist]
        - roots: a list a_0, a_1, ..., a_n where a_i*a_i - N can be factored
                 over primeset
        - rowlist: a list such that rowlist[i] is a
                   primeset-vector over GF(2) corresponding to a_i
          such that len(roots) = len(rowlist) and len(roots) > len(primeset)
    '''
    x = intsqrt(N) + 2
    roots = []
    rowlist = []
    while len(roots) <= len(primeset):
        y = x*x - N
        tmprow = dumb_factor(y, primeset)
        if tmprow != []:
            roots.append(x)
            rowlist.append(make_Vec(primeset, tmprow))
        x += 1
    return (roots, rowlist)



## Task 4
def find_a_and_b(v, roots, N):
    '''
    Input: 
     - a {0,1,..., n-1}-vector v over GF(2) where n = len(roots)
     - a list roots of integers
     - an integer N to factor
    Output:
      a pair (a,b) of integers
      such that a*a-b*b is a multiple of N
      (if v is correctly chosen)
    '''

    alist = [roots[x] for x in v.D if v[x] != 0]
    a = prod(alist)
    c = prod(map(lambda x: x*x-N, alist))
    b = intsqrt(c)
    return (a, b)

## Task 5
N = 2461799993978700679

def factor(N):
    ret = []
    print('N=', N)
    primeset = primes(10000)
    primelist = list(primeset)
    #shuffle(primelist)
    primelist.sort(reverse=True)
    roots, rowlist = find_candidates(N, primeset)
    M = echelon.transformation_rows(rowlist)
    for i in reversed(range(len(M))):
        a, b = find_a_and_b(M[i], roots, N)
        if gcd(a-b, N) != 1:
            print('find ', gcd(a-b, N))
            ret.append(gcd(a-b, N))
            N //= gcd(a-b, N)
        if N == 1:
            break
    return ret

smallest_nontrivial_divisor_of_2461799993978700679 = 1230926561
