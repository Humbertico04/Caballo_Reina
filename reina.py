def posicion_reina(n):
    posicion = []
    for i in range(n+1):
        if i%2 == 0 and i != 0:
            posicion.append(i)
    for i in range(n+1):
        if i%2 != 0 and i != 0:
            posicion.append(i)
    return posicion

def matriz(n):
    tablero=[]
    for i in range(n):
        tablero.append([0]*n)
    return tablero

def tablero_solucion(n):
    tablero = matriz(n)
    posición = posicion_reina(n)
    for i in range(len(tablero)):
        tablero[posición[i]-1][i] = 1
    return tablero

print(tablero_solucion(10))


[[0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]