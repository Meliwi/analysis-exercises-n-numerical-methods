import math
from decimal import Decimal
# This function finds the absolute and relative error.
total = 0
def error(n,m):
  absoluto = abs(n - m)
  print("error absoluto es", absoluto)
  relativo = absoluto /n *100
  print("error relativo es", relativo)
  return 0;

error(math.pi , 22/7)
error(math.pi , 3.1416)
error(math.e , 2.718)
error(10**math.pi , 1400)
error(1.0,1.0000000000000007)





