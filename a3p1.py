"""
Name: Niki Zheng
W0470221

Assignment 3
Program 1
"""
"""
Requirement:
A- All positive numbers that are divisible by 10 and less than n. 
For example, if n is 100, print 10 20 30 40 50 60 70 80 90.
Note: Use a function called printPositiveNumbers to perform this loop 
    by passing the value of n.
B- All powers of two less than n. For example, if n is 100, print 1 2 4 8 16 32 64.
Note: Use a function called printPowersOfTwo to perform this loop by passing 
    the value of n.
"""

"""
Step 1: Define the function.
Step 2: Import the limitation number.
"""
# A Part
def printPositiveNumbers(n): # n is the global variable
    print(f"The positive numbers under {n} are: ")
    i = 1
    while i < n:
        if i % 10 == 0:
            print(i, end="\t")
        i = i + 1
printPositiveNumbers(100) # 100 is the local variable
print("\n")

# B part
def printPowerOfTwo(n): # n is the global variable
    print(f"The powers of two under {n} are: ")
    j = 0
    while j < n:
        if 2 ** j < n:
            print(2 ** j,end="\t")
        j = j + 1
printPowerOfTwo(100) # 100 is the local variable
print("\n")

# Modify part
def nDivBym(n,m):
    print(f"Numbers under {n} can be divided by {m} are:")
    i = 1
    while i < n:
        if i % m == 0:
            print(i,end="\t")
        i = i + 1
nDivBym(100,5)
