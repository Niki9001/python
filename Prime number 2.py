"""
Judge whether the input number is a prime number or not
Author: Niki Zheng

"""
a = int(input("Please input a number over 1: "))
while a <= 1:
    print("Please input again")
    a = int(input("Please input a number over 1: "))
b = 2
flag = True
while b < a:
    if a % b == 0:
        flag = False
    b = b + 1
if flag == True:
    print(f"{a} is True")
else:
    print(f"{a} is not True")
