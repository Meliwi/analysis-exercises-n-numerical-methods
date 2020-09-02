# Esta función estima el valor de e^x con x = 0.5 con al menos 3 cifras significativas

import math

def euler_function(n):
    e = 0
    for i in range (21):
        e = round(e + n**i/math.factorial(i),3)
    return e

value= euler_function(2)
print(value)