# Intento de buscar soluciones automaticamente para el problema de las reinas, quedó en ver como se mueve la reina

import numpy as np

#Crea matriz de ceros nxn
def matriz(n):
    tablero=np.zeros((n,n))
    return tablero

#Dada la posición de la reina y un tablero nxn muestra con 1 las posiciones a las que puede moverse
def mov_reina(n, posición):
    matrizn=matriz(n)
    #Si está en la misma fila o columna que la reina reemplaza por 1
    for i in range(n):
        for j in range(n):
            if matrizn[i][j] != 2  and i==posición[0] or j==posición[1] :
                matrizn[i][j]=1
    #Si está en la misma diagonal que la reina reemplaza por 1
    for i in range(n):
        for j in range(n):
            if matrizn[i][j] != 2 and i-j==posición[0]-posición[1] or i+j==posición[0]+posición[1]:
                matrizn[i][j]=1
    return matrizn

mov_reina(6, [1, 0])
