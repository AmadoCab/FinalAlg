# Coordenadas en x de los vertices
pol_ver_x = [0, 1, 2]
# Coordenadas en y de los vertices
pol_ver_y = [0, 2, 0]

# Punto a evaluar
point_x, point_y = (1,1)

# Función
def testPointInPolygon(pol_ver_x, pol_ver_y, point_x, point_y):
    n = len(pol_ver_x)
    count = 0
    x, y = point_x, point_y

    for i in range(n-1):
        ax, ay = pol_ver_x[i], pol_ver_y[i]
        bx, by = pol_ver_x[i+1], pol_ver_y[i+1]
        if ((y > ay) != (y > by)) and (x < (y-ay)*(ax-bx)/(ay-by)+ax):
            count += 1
    return count%2 != 0

# Llamando a la función
print(testPointInPolygon(pol_ver_x,pol_ver_y,point_x,point_y))

# EOF #
