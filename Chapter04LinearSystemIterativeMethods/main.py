from GS import GS
from Jacobi import Jacobi
from SOR import SOR
import numpy as np

A = np.array([[3,-1,1],[1,-8,-2],[1,1,5]])
b = np.array([-2,1,4])

x1 = SOR(A,b,100,1e-6,1.075)
x2 = Jacobi(A,b,20,1e-6)
x3 = GS(A,b,20,1e-6)