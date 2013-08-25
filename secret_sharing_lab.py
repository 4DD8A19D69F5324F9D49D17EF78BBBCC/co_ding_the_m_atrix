# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from itertools import combinations
from independence import is_independent

## Problem 1
def randGF2(): return random.randint(0, 1) * one


a0 = list2vec([one, one, 0, one, 0, one])
b0 = list2vec([one, one, 0, 0, 0, one])


def choose_secret_vector(s, t):
    while True:
        rv = list2vec([randGF2() for i in range(6)])
        if a0*rv == s and b0*rv == t:
            return rv


## Problem 2
# Give each vector as a Vec instance
while True:
    secret_a0 = list2vec([0, 0, 0, 0, 0, one])
    secret_b0 = list2vec([0, 0, 0, 0, one, 0])
    secret_a1 = list2vec([0, 0, 0, one, 0, 0])
    secret_b1 = list2vec([0, 0, one, 0, 0, 0])
    secret_a2 = list2vec([0, one, 0, 0, 0, 0])
    secret_b2 = list2vec([one, 0, 0, 0, 0, 0])
    secret_a3 = list2vec([randGF2() for i in range(6)])
    secret_b3 = list2vec([randGF2() for i in range(6)])
    secret_a4 = list2vec([randGF2() for i in range(6)])
    secret_b4 = list2vec([randGF2() for i in range(6)])
    vecs = [(secret_a0, secret_b0),(secret_a1,secret_b1),(secret_a2,secret_b2),(secret_a3,secret_b3),(secret_a4,secret_b4)]
    if all(is_independent(list(sum(x,()))) for x in combinations(vecs,3)):
        break