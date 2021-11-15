# Matriz en la que buscar los puntos silla
matrix = [[ 1,10,3 ,2 ,5 ],
	  [-1, 1,4 ,3 ,7 ],
	  [ 0, 2,3 ,6 ,3 ],
	  [ 1, 8,4 ,6 ,2 ],
	  [ 0, 4,-1,5 ,1 ]]

# Función
def get_cPoint(matrix):
    for i in range(1, len(matrix)-1):
        for j in range(1,len(matrix[0])-1):
            if (matrix[i+1][j] >= matrix[i][j] and matrix[i-1][j] >= matrix[i][j]):
                if (matrix[i][j+1] <= matrix[i][j] and matrix[i][j-1] <= matrix[i][j]):
                    return (i,j)
            elif (matrix[i+1][j] <= matrix[i][j] and matrix[i-1][j] <= matrix[i][j]):
                if (matrix[i][j+1] >= matrix[i][j] and matrix[i][j-1] >= matrix[i][j]):
                    return (i,j)
    return None

# Llamando a la función 
ans = get_cPoint(matrix)
print(f"{ans[0]+1} {ans[1]+1}")

# EOF #
