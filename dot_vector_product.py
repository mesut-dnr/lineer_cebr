# -*- coding: utf-8 -*-
import numpy as np
import scipy.linalg as lin

matrix2d = np.array([
    [100,200,300],
    [400,500,600],
    [700,800,900]
    ])

# inverse=lin.inv(matrix2d)
# print('Matriksin Tersi:')
# print(inverse)

# determinant=lin.det(matrix2d)
# print('Determinant:')
# print(determinant)

vector=np.array([25,50,75])

dot=matrix2d.dot(vector)
print('Noktasal:')
print(dot)                  


ozdegerler =lin.eig(matrix2d)
print('Özdeğerler:')
print(ozdegerler)