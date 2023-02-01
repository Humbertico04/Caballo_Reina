def rama_siguiente(lista):
    a=[[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]
    b=[]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            b.append(a[lista[i][j]])
    return b

a=[[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]

dic_prev = {0: 2, 1: 2, 2: 2, 3: 2, 4: 3, 5: 0, 6: 3, 7: 2, 8: 2, 9: 2}
dic= {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

print(dic_prev/2)
def contador_por_dic(dic_prev, dic):
    contador = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            for k in range(len(a[a[i][j]])):
                dic[a[a[i][j]][k]] += dic_prev[i]
                contador += dic_prev[i]
    return contador, dic
print(contador_por_dic(dic_prev, dic))
def n_dic(n):
    dic_prev = {0: 2, 1: 2, 2: 2, 3: 2, 4: 3, 5: 0, 6: 3, 7: 2, 8: 2, 9: 2}
    for i in range(n):
        dic= {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        cont, dic = contador_por_dic(dic_prev, dic)
        print("{}:".format(i*2+3), cont)
        dic_prev=dic

n_dic(3)

# a, b= contador_por_dic(dic_prev, dic)
# print(b)
# contador_por_dic(b, dic)




















