# Implementación del algoritmo de Jacobi
import numpy as np
def jacobi(A,b,x0):
  eps = 1e-20
  n = 100
  D = np.diag(np.diag(A))
  LU = A-D
  x = x0
  for i in range(n):
    D_inv = np.linalg.inv(D)
    xTemp = x
    #np.dot multiplicación de matrices, formula que describe el método
    x = np.dot(D_inv,np.dot(-(LU),x)+b)
    print('paso: ',i,'-x:',x)
    # Función de numpy para hallar la norma de una matriz
    if np.linalg.norm(x-xTemp) <eps:
      return x
  return x

A = np.array([
  [5,2,1,1],
  [2,6,2,1],
  [1,2,7,1],
  [1,1,2,8]
])

b = np.array([29,31,26,19])
x0 = np.random.rand(4)
x = jacobi(A,b,x0)

print('x:',x)
print('b calculado: ',np.dot(A,x))
print('b verdadero: ',b)
