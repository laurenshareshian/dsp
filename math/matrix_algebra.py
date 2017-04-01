# Matrix Algebra

import numpy as np
from scipy import linalg


A=np.matrix([[1,2,3],[2,7,4]])
B=np.matrix([[1,-1],[0,1]])
C=np.matrix([[5,-1],[9,1],[6,0]])
D=np.matrix([[3,-2,-1],[1,2,3]])
E=np.matrix([[3,2,4],[2,0,2], [4,2,3]])

u=np.array([6,2,-3,5])
v=np.array([3,5,-1,4])
w=np.array([[1],[8],[0],[5]])
z=np.array([[1], [8], [0]])

print(A.shape)
print(u.shape)
print(u+v)
print(np.dot(u,v))
print(linalg.norm(u))
print(A+C.T)
print(A*z)
print(linalg.inv(E))
print(linalg.eig(E))