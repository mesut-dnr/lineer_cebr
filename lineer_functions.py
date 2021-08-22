# -*- coding: utf-8 -*-
import numpy as np
import scipy.linalg as lin

matrix2d = np.array([
    [100,200,300],
    [400,500,600],
    [700,800,900]
    ])

logarithm=lin.logm(matrix2d)
print('Logaritma:')
print(logarithm)

ussel=lin.expm(matrix2d)
print('Üssel:')
print(ussel)

sin=lin.sinm(matrix2d)
print('Sinüs:')
print(sin)
