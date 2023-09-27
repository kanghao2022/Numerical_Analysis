from Gauss import Gauss
from LUdecomposition import LU_Doolittle_decomp
import numpy as np

A = np.array([[3,1,2], [6, 3 ,4], [3, 2, 5]])
b = np.array([11,24,22])
x1 = LU_Doolittle_decomp(A,b)
x2 = LU_Doolittle_decomp(A,b)
print("Lu分解的解为",x1)
print("LU分解计算方程组的残差为：",np.linalg.norm(A@x1-b))
print("Gauss消去的解为",x2)
print("Gauss消去计算方程组的残差为：",np.linalg.norm(A@x2-b))

def Hilbert_Matrix(i,j):
    H = np.zeros((i,j))
    for i in range(1,i+1):
        for j in range(1,j+1):
            H[i-1,j-1] = 1/(i+j-1)
    return H

H_12 = Hilbert_Matrix(12,12)
H_20 = Hilbert_Matrix(20,20)
b_12 = H_12@np.ones((12,1))
b_20 = H_20@np.ones((20,1))

x=LU_Doolittle_decomp(H_20,b_20)
print("LU分解求解结果:")
print(x)
print("LU分解残差:")
print(np.linalg.norm(H_20@x-b_20))
x = Gauss(H_20, b_20)
print("Gauss求解结果:")
print(x)
print("Gauss残差:")
print(np.linalg.norm(H_20@x-b_20))