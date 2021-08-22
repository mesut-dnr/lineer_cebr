# -*- coding: utf-8 -*-
import numpy as np
import scipy.linalg as lin

# Lineer Denklemler
# # 3x1 + 5x2 + 7x3 = 10
# # 2x1 + 4x2 + 8x3 = 14
# # 5x1 + 12x2 + 13x3 = 5

A=np.array([     #Katsayılar Matriksi
    [3,5,7],
    [2,4,8],
    [5,12,13]    
])

B=np.array([10,14,5]) #Değerler

lineer_solution=lin.solve(A,B)
print('Lineer Çözüm:')
print(lineer_solution)