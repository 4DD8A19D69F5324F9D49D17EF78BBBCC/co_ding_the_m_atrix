# version code 988
# Please fill out this stencil and submit using the provided submission script.

import doctest

from matutil import *
from vecutil import *
from GF2 import one
import echelon



## Problem 1
# Write each matrix as a list of row lists

echelon_form_1 = [[1, 2, 0, 2, 0],
                  [0, 1, 0, 3, 4],
                  [0, 0, 2, 3, 4],
                  [0, 0, 0, 2, 0],
                  [0, 0, 0, 0, 4]]

echelon_form_2 = [[0, 4, 3, 4, 4],
                  [0, 0, 4, 2, 0],
                  [0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0]]

echelon_form_3 = [[1, 0, 0, 1],
                  [0, 0, 0, 1],
                  [0, 0, 0, 0]]

echelon_form_4 = [[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]



## Problem 2
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
    '''
    p = -1
    for l in A:
        flag = False
        for idx, item in enumerate(l):
            if item != 0:
                if idx > p:
                    p = idx
                    flag = True
                    break
                else:
                    return False
        if not flag:
            p = len(l) + 1
    return True


## Problem 3
# Give each answer as a list

echelon_form_vec_a = [1, 0, 3, 0]
echelon_form_vec_b = [-3, 0, -2, 3]
echelon_form_vec_c = [-5, 0, 2, 0, 2]



## Problem 4
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None".

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21, 0, 2, 0, 0]



## Problem 5
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
    >>> b_list = [one,0,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> s = echelon_solve(U_rows, cols, b_list)
    >>> rowdict2mat(U_rows) *s == list2vec(b_list)
    True
    '''
    ret = Vec(set(label_list), {})
    for i, row in enumerate(reversed(rowlist)):
        t = b[len(b) - i - 1]
        for x in label_list:
            t += row[x] * ret[x]
        if t == one:
            for x in label_list:
                if row[x] == one:
                    ret[x] = one
                    break
    return ret


## Problem 6


def solve(A, b):
    col_label_list = sorted(A.D[1])
    M = echelon.transformation(A, col_label_list)
    U = M*A
    U_rows_dict = mat2rowdict(U)
    rowlist = [U_rows_dict[i] for i in U_rows_dict]
    x = M*b
    return echelon_solve(rowlist, col_label_list, [x[item] for item in x.D])

D = {'A', 'B', 'C', 'D'}
A = Mat(({'a', 'b', 'c', 'd'}, {'A', 'B', 'C', 'D'}),
        {('a', 'B'): one, ('a', 'C'): 0, ('d', 'C'): one, ('a', 'A'): one, ('d', 'D'): one, ('d', 'A'): 0,
         ('d', 'B'): 0, ('b', 'B'): 0, ('c', 'B'): one, ('a', 'C'): 0, ('c', 'A'): one, ('b', 'D'): one,
         ('c', 'D'): one, ('c', 'C'): one, ('b', 'A'): one, ('a', 'D'): one})

r = Vec({'a', 'b', 'c', 'd'}, {'a': one, 'c': one})


col_label_list = sorted(A.D[1])
M = echelon.transformation(A)
U = M*A
U_rows_dict = mat2rowdict(U)
x = M*r


rowlist = [U_rows_dict[i] for i in U_rows_dict]
label_list = col_label_list
b = [x[item] for item in x.D]


## Problem 7
null_space_rows_a = {3, 4} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {4}



## Problem 9
# Write each vector as a list
closest_vector_1 = [8.0/5, 16.0/5]
closest_vector_2 = [0, 1, 0]
closest_vector_3 = [3, 2, 1, -4]



## Problem 10
# Write each vector as a list

project_onto_1 = [2, 0]
projection_orthogonal_1 = [0, 1]

project_onto_2 = [-1.0/6, -1.0/3, 1.0/6]
projection_orthogonal_2 = [7.0/6, 4.0/3, 23.0/6]

project_onto_3 = [1, 1, 4]
projection_orthogonal_3 = [0, 0, 0]



## Problem 11
norm1 = 3
norm2 = 4
norm3 = 1

if __name__ == '__main__':
    doctest.testmod()