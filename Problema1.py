from math import sqrt

# Función de la distancia Euclideana
def d(a,b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

# Función h mencionada en la definición de Hausdorff
def h(A,B):
    supval = 0
    for a in A:
        infval = 'None'
        for b in B:
            if infval == 'None':
                infval = d(a,b)
            else:
                infval = min(infval,d(a,b))
        supval = max(supval,infval)
    return supval

# Función de Hausdorff
def H(A,B):
    return max(h(A,B),h(B,A))

# Aquí se pueden definir los conjuntos X y Y del enunciado
X = [
    (1,1), (0,0)
]
Y = [
    (1,-1), (0,0)
]

# Se llama a la función y se regresa el resultado
print(H(X,Y))

# EOF #

