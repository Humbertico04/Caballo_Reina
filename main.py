a=[[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]

suma=0
for i in range(len(a)):
    suma+=len(a[i])
print(suma)

b=[]
for i in range(len(a)):
    for j in range(len(a[i])):
        b.append(a[a[i][j]])
print(b)