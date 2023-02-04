# Halla una solución posible al problema de las n reinas y la muestra en un tablero de ajedrez a color

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
    tablero = matriz(n)
    posición = posicion_reina(n)
    for i in range(len(tablero)):
        tablero[posición[i]-1][i] = 1
    return tablero

#Utiliza el tablero de la función anterior para mostrarlo en un tablero de ajedrez a color
def tablero_con_reina(n):
    a = [0,1]
    for i in range(len(tablero_solucion(n))):
        for j in range(len(tablero_solucion(n))):
            if tablero_solucion(n)[i][j] == 1:
                print("\033[42m"+"  "+'\033[0;m', sep="", end="")
            else:     
                if i % 2 == a[j % 2]: 
                    print("\033[47m"+"  "+'\033[0;m', sep="", end="")
                else:  
                    print("\033[40m"+"  "+'\033[0;m', sep="", end="")
        print("")

print("Solución para el problema de reinas a color:")
tablero_con_reina(10)

if __name__ == "__main__":
    main()
