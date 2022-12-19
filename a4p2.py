"""
Name: Niki Xiaoning Zheng
W0470221
Assignment 4 Program 2
"""

def factorial(n):
    i = 1
    j = n
    while i < n:
        j = j * i
        i = i + 1
    return j

    #print(f"The factorial value of {n} is: {j}")
EnterNum = int(input("Enter the value of N: "))
factorial(EnterNum)
r = factorial(EnterNum)
print(f"The factorial value of {EnterNum} is {r}")