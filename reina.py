# Crea matriz de 0's 7x7
def matriz(n):
    a=[]
    for i in range(n):
        a.append([0]*n)
    return a

def mov_reina(a, posición):
    #Si esta en la misma fila o columna que la reina reemplaza por 1
    for i in range(len(a)):
        for j in range(len(a)):
            if i==posición[0] or j==posición[1]:
                a[i][j]=1
    #Si esta en la misma diagonal que la reina reemplaza por 1
    for i in range(len(a)):
        for j in range(len(a)):
            if i-j==posición[0]-posición[1] or i+j==posición[0]+posición[1]:
                a[i][j]=1
    return a
a= mov_reina(matriz(7), [1, 0])
print(a)

#Recorre la matriz buscando 0
def busca_ceros(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j]==0:
                return True
    return False

print(busca_ceros(a))

[[1, 1, 0, 0, 0, 0, 0], 
 [1, 1, 1, 1, 1, 1, 1], 
 [1, 1, 0, 0, 0, 0, 0], 
 [1, 0, 1, 0, 0, 0, 0], 
 [1, 0, 0, 1, 0, 0, 0], 
 [1, 0, 0, 0, 1, 0, 0], 
 [1, 0, 0, 0, 0, 1, 0]]