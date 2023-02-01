a=[[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]

def suma_elementos(lista):
    suma=0
    for i in range(len(lista)):
        suma+=len(lista[i])
    return suma

def n_siguiente(lista):
    b=[]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            b.append(lista[lista[i][j]])
    return b

b=n_siguiente(a)
print(b)
print(suma_elementos(b))