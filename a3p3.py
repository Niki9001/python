"""
Name: Niki Zheng
W0470221

Assignment 3
Program 2
"""
"""
Requirement:
Write program that read a sequence of integer inputs and print:
A- The smallest and largest of the inputs. (2.5 marks)
B- The number of even inputs.
"""
"""
Step 1: Define the function.
Step 2: Import the limitation number.
"""
def maxAndMin(n):
    imax = 0
    imin = float("inf")
    i = 0
    j = 0
    even = 0
    odd = 0
    while j < 1:
        j = j + 1
        while i < a:
            num = float(input("Enter: "))
            if num > imax:
                imax = num
            if num < imin:
                imin = num
            i = i + 1
            if i % 2 == 0:
                even = even + 1
            else:
                odd = odd + 1
        print(f"The largest number is {imax}, and the smallest number is {imin}")
    print(f"The number of even time inputs is {even}.")
    # Enhanced
    print(f"The number of odd time input is {odd}.")
a = int(input("How many times enter: "))
maxAndMin(a)