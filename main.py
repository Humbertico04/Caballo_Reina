#Suma todos los elementos que hay
def suma_elementos(lista):
    suma=0
    for i in range(len(lista)):
        suma+=len(lista[i])
    return suma

#Calcula los elementos de la siguiente lista en el árbol
def rama_siguiente(lista):
    a=[[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]
    b=[]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            b.append(a[lista[i][j]])
    return b

#Calcula los elementos del árbol hasta el n-ésimo nivel
def n_ramas(n):
    a=[[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]
    for i in range(n):
        b=rama_siguiente(a)
        print(b)
        print("{}:".format(i+1), suma_elementos(a))
        a=b

n_ramas(5)


















# b=n_siguiente(a)
# print(b)
# print(suma_elementos(b))

# c=n_siguiente(b)
# print(c)
# print(suma_elementos(c))

# d=n_siguiente(c)
# print(d)
# print(suma_elementos(d))