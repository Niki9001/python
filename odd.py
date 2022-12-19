"""
Name: Niki Xiaoning Zheng
W0470221
Function excises 2
Odd number

"""
"""
Step 1: Input the mark
Step 2: Processing with conditions
Step 3: Output
"""
a = int(input("Please enter a number: "))
def number_id(b):
    if a %2 == 1 and a > 0:
        return "This is an odd"
    else:
        return "This is not an odd"
print(number_id(a))