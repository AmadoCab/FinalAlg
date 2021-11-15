# Arreglo de numeros
A = [1,-1,3,0,8]

# Función
def get_minabs(l):
    l = sorted(l)
    minval = l[1] - l[0]
    for i in range(2,len(A)):
        minval = min(minval, l[i]-l[i-1])
    return minval

# Llamando a la función
print(get_minabs(A))

# EOF #
