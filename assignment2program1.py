"""
Name: Niki Xiaoning Zheng
W0470221
Assignment 2 program 1

"""
"""
Step 1: Enter data of this program
Step 2: Calculate the result with conditions
Step 3: Throwing error when users input wrong data.
Step 4: Output

"""

houseNumber = int(input("Enter House Number: "))
depthOfLand = float(input("Enter property depth (feet): "))
widthOfLand = float(input("Enter property width (feet): "))
grassKind = str(input("Enter type of grass (fescue, bentgrass, campus): ").lower())
if grassKind == "fescue":
    pricePerSqft = 0.05
elif grassKind == "bentgrass":
    pricePerSqft = 0.02
elif grassKind == "campus":
    pricePerSqft = 0.01
else:
    print("You entered an invalid grass type. Please try it again.")
    exit()
numberOfTrees = int(input("Enter the number of trees: "))
labourFee = 1000
surface = depthOfLand * widthOfLand
treeprice = numberOfTrees * 100
if surface > 5000:
    addtionalFee = 500
else:
    addtionalFee = 0
totalcost = surface * pricePerSqft + treeprice + labourFee + addtionalFee
print("Total cost for house", houseNumber, "is: {0:.2f}".format(totalcost))