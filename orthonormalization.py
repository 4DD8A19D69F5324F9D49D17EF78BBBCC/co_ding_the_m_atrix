from orthogonalization import orthogonalize,aug_orthogonalize
from math import sqrt
from matutil import *

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    olist = orthogonalize(L)
    return [ o/sqrt(o*o) for o in olist]




def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    Qlist = orthonormalize(L)
    Qtmat = coldict2mat(Qlist).transpose()
    Rmat = Qtmat*coldict2mat(L)
    Rlist = list(mat2coldict(Rmat).values())
    return Qlist,Rlist
