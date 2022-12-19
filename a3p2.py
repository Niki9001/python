"""
Name: Niki Zheng
W0470221

Assignment 3
Program 2
"""
"""
Requirement:
Write a loop statement that computes:
A- The sum of all even numbers between 2 and 200 (inclusive).
Note: Use function called sumOfEvenNumbers to perform this loop.
B- The sum of all squares between 1 and 200 (inclusive). 
Use function called sumOfSquares to perform this loop.
"""
"""
Step 1: Define the function.
Step 2: Import the limitation number.
"""

# Part A
def sumOfEvenNumbers(n):
    i = 0
    j = 0
    while i < n:
        i = i + 1
        if i % 2 == 0:
            #print(i)
            j = j + i
    print(f"Sum of even numbers under {n} is {j}.")
sumOfEvenNumbers(200)

# Part B
def sumOfSquares(n):
    i = 1
    j = 0
    while i <= n:
        j = j + i ** 2
        i = i + 1
    print(f"Sum of squares under {n} is {j}.")
sumOfSquares(200)

# Modify part
def sumOfEvenNoExpm(n,m):
    i = 0
    j = 0
    while i < n:
        i = i + 1
        if i != m:
            if i % 2 == 0:
                j = j + i
        else:
            j = j
    print(f"Sum of numbers under {n} except {m} is {j}.")

sumOfEvenNoExpm(200,100)