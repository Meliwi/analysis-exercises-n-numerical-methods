suma = 0.0
for i in range(0,100):
    suma = suma + 1/100
print(str(suma))

#calculate relative and absolute error

def absErrorlimit (n):
    absoluteLimit = 1 / (2 * (pow(10,n)))
    print("El error absoluto acotado es: ",absoluteLimit)
    return 0;

# using 16 significant numbers
absErrorlimit(16)

# Relative error
print("El error relativo acotado es: ", (1/ (2 * (pow(10,16))))/ 1.0000000000000007)