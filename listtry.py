import random
"""
matr = []
list1 = [[random.randint(1,100)]*5]*5

list_three = [[0 for i in range(3)] for j in range(3)]
print(list_three)
list_three[1][1] = 3
print(list_three)
"""
"""
import numpy as np
from array import *
matrix = []
def ranTest():
    a = np.random.randint(1,100,size=(5,5))
    print(a)
matrix = [ranTest()]


print(matrix[1])
"""
"""
Two ways to solve this question
"""
# Way 1
matric = []
def matric1(a,b):
    for i in range(a):
        for j in range(b):
            matric.append(j)
            print()
            j = j + 1
        i = i + 1
        matric.append(i)
    print(matric)
matric1(5,4)

print("\n")
# Way 2
def matric(a,b):
    i = 0
    while i < a:
        j = 0
        while j < b:
            j = j + 1
            print(random.randint(1,100),end="\t")
        i = i + 1
        print(random.randint(1,100))
M = [matric(5,4)]
