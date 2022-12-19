"""
Name: Niki Xiaoning Zheng
W0470221

"""
import random
matrx = []
for i in range (5):
    matric = []
    for j in range (5):
        a = random.randint(1,100)
        j = j + 1
        matric.append(a)
    i = i + 1
    matrx.append(matric)

print(matrx)

#print(matrx[1][1])
print("\n")

for k in range (5):
    for l in range (5):
        print(matrx[k][l],end="\t")
        l = l + 1
    print()
    k = k + 1


