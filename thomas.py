# Algoritmo de Thomas o algoritmo para matrices tridiagonales

def thomas_alg(a,b,c,d):
    #hallamos el número de filas
    n = len(d)
    #Modifica los coeficientes de la primera fila
    c[0]/=b[0]
    d[0]/=b[0]
    for i in range (1,n):
        ptemp = b[i] - a([i]*c[i-1])
        c[i] /= ptemp
        d[i] = (d[i]-a[i]*d[i-1])/ptemp
    #Sustitución hacia atrás
    x = [0 for i in range(n)]
    x[-1] = d[-1]
    for i in range (-2,-n-1,-1):
        x[i] = d[i] - c[i] *x[i+1]
    return x

