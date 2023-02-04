import numpy as np

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
    tablero=np.zeros((n,n))
    return tablero

def tablero_solucion(n):
    tablero = matriz(n)
    posición = posicion_reina(n)
    for i in range(len(tablero)):
        tablero[posición[i]-1][i] = 1
    return tablero

print(tablero_solucion(6))


def fila(n, color_inic):
    # 0 para iniciar la fila con blanco, 1 para negro
    for i in range(n):      
        if i % 2 == color_inic: 
            print("\033[47m"+"  "+'\033[0;m', sep="", end="")
        else:  
            print("\033[40m"+"  "+'\033[0;m', sep="", end="")


def borde():
    print("\033[44m"+"  "+'\033[0;m', sep="", end="")

def borde_sup_inf(n):
    for i in range(n+2):
        borde()
    print("")
  
def fila_completa(n):
    for i in range(n):
        borde()
        fila(n, i%2) 
        borde() 
        print("")

def tablero(n):
    borde_sup_inf(n)

    fila_completa(n)

    borde_sup_inf(n)




tablero(5)

 


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