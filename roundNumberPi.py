# round the number pi to the thousandths and limit absolute and relative errors

import math
round(math.pi,3)
# absolute error
def absErrorlimit (n):
    absoluteLimit = 1 / (2 * (pow(10,n)))
    print("El error absoluto acotado es: ",absoluteLimit)
    return 0;
# using 3 significant numbers
absErrorlimit(4)

# Relative error
print("El error relativo acotado es: ", 0.0005/ round(math.pi,3))

# Then our number is 3.142 +- 0.0005

