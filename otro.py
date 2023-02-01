#Suma todos los elementos que hay
def suma_elementos(lista):
    return sum(len(lista[i]) for i in range(len(lista)))

#Calcula los elementos de la siguiente lista en el árbol
def rama_siguiente(lista):
    a=[[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]
    return [a[i] for sublista in lista for i in sublista]

#Calcula los elementos del árbol hasta el n-ésimo nivel
def n_ramas(n):
    a=[[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]
    for i in range(n):
        b=rama_siguiente(a)
        print("{}:".format(i+1), suma_elementos(a))
        a=b

n_ramas(20)

