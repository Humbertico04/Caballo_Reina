a=[[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]

def suma_elementos(lista):
    suma=0
    for i in range(len(lista)):
        suma+=len(lista[i])
    return suma

def n_siguiente(lista):
    a=[[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]
    b=[]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            b.append(a[lista[i][j]])
    return b

def n_algo(n):
    a=[[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]
    for i in range(n-1):
        b=n_siguiente(a)
        print("{}:".format(i+2), suma_elementos(b))
        a=b

n_algo(30)
# b=n_siguiente(a)
# print(b)
# print(suma_elementos(b))

# c=n_siguiente(b)
# print(c)
# print(suma_elementos(c))

# d=n_siguiente(c)
# print(d)
# print(suma_elementos(d))