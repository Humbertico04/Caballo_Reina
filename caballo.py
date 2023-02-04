# Versión optimizada para resolver el problema de los caballos (límite: n = 11957)

from ast import main

#Avanza en el árbol de soluciones dos niveles por vez
def contador_por_dic(dic_prev, dic):
    contador = 0
    a = [[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]
    for i in range(len(a)):
        for j in range(len(a[i])):
            for k in range(len(a[a[i][j]])):
                dic[a[a[i][j]][k]] += dic_prev[i]
                contador += dic_prev[i]
    return contador, dic

#Calcula los elementos del árbol hasta el n-ésimo nivel
def n_dic(n):
    dic_prevpar = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
    dic_previmpar = {0: 2, 1: 2, 2: 2, 3: 2, 4: 3, 5: 0, 6: 3, 7: 2, 8: 2, 9: 2}
    for i in range(n//2):
        dicp = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        cont, dicp = contador_por_dic(dic_prevpar, dicp)
        print("{}:".format(i*2+2), cont)
        # print(dicp, "\n") #Descomentar para ver los diccionarios intermedios pares
        dic_prevpar=dicp
        dici = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        cont, dici = contador_por_dic(dic_previmpar, dici)
        print("{}:".format(i*2+3), cont)
        # print(dici, "\n") #Descomentar para ver los diccionarios intermedios impares
        dic_previmpar=dici
    return cont

print("Solución para el problema de los caballos:")        
n_dic(33)

if __name__ == "__main__":
    main()