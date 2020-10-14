import numpy as np
# Método de Jacobi
def jacobi(A,x0,b):
  eps = 1e-20
  n = 100
  # Crear la matriz Q con solo las diagonales
  Q = np.diag(np.diag(A))
  # Suma de los coeficientes de la fila excluyendo la digonal
  S = np.sum(np.abs(A), axis=1) - Q
  # Construimos la matriz identidad
  I = np.identity(A.shape[1])
  # Hallamos la matriz inversa
  Q_inv = np.linalg.inv(Q)
  # Hacemos la operación
  f_op = I-np.dot(Q_inv,A)
  # Verificamos que algunas de las dos condiciones se cumpla
  if np.all(Q>S) or np.linalg.norm((np.linalg.norm(f_op,1))<1):
    x = x0
    for i in range (n):
      x_temp = x
      x = np.dot(f_op,x) + np.dot(Q_inv,b)
      print (x)
      if np.linalg.norm(x-x_temp) < eps:
        return x
    return x
  else:
      print("La matriz no cumple con alguna de las condiciones")

#Prueba con la matriz
A = np.array([
  [10,1,2,3,4],
  [1,9,-1,2,-3],
  [2,-1,7,3,-5],
  [3,2,3,12,-1],
  [4,-3,-5,-1,15]
])

b = np.array([12,-27,14,-17,12])
x0 = np.array ([0,0,0,0,0])
x = jacobi(A,x0,b)
