"""
Name: Niki Xiaoning Zheng
W0470221
Assignment 2 program 2
"""
"""
Step 1: Define rate calculate function
Step 2: Input usage
Step 3: Output result
"""

def estRate(useage):
    if useage <= 200:
        price = 20
    elif useage > 200 and useage <= 500:
        price = useage * 0.105
    elif useage > 500 and useage <= 1000:
        price = useage * 0.110
    else:
        price = 118
    print("Total charge is $ {0:.2f}".format(price))
userInput = int(input("Enter data usage (Mb): "))
estRate(userInput)