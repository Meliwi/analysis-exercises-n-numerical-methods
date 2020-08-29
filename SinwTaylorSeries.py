import math

def sin_fun(n):
  x = math.radians(n)
  sin_x = 0
  for i in range(11):
    sin_x = sin_x + pow(-1,i) * pow(x,2*i+1)/math.factorial((2*i+1))
  return sin_x

# using the function sin
out = sin_fun(45)
print(out)

