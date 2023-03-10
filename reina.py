# Halla una solución posible al problema de las n reinas

import numpy as np
from ast import main

#Para toda n - [2, 3], crea una lista con una solución posible del problema de las n reinas
def posicion_reina(n):
    posicion = []
    for i in range(n+1):
        if i%2 == 0 and i != 0:
            posicion.append(i)
    for i in range(n+1):
        if i%2 != 0 and i != 0:
            posicion.append(i)
    return posicion

#Crea matriz de ceros nxn
def matriz(n):
    tablero=np.zeros((n,n))
    return tablero

#Crea un tablero con unos en las posiciones de las reinas de una solución posible, rellena el resto con ceros
def tablero_solucion(n):
    if n == 2 or n == 3:
        return "No hay solución para n = {}". format(n)
    tablero = matriz(n)
    posición = posicion_reina(n)
    for i in range(len(tablero)):
        tablero[posición[i]-1][i] = 1
    return tablero

print("Solución para el problema de reinas:")   
print(tablero_solucion(10))

if __name__ == "__main__":
    main()
