"""
Name: Niki Xiaoning Zheng
W0470221
Assignment 2 program 1

"""
"""
Step 1: Define function
Step 2: Input data
Step 3: Calling function
Step 4: Output

"""
def calculationOfTotalCost(houseNumber,depthOfLand,widthOfLand,grassKind):

    if grassKind == "fescue":
        pricePerSqft = 0.05
    elif grassKind == "bentgrass":
        pricePerSqft = 0.02
    elif grassKind == "campus":
        pricePerSqft = 0.01

    labourFee = 1000
    surface = depthOfLand * widthOfLand
    treeprice = numberOfTrees * 100
    if surface > 5000:
        addtionalFee = 500
    else:
        addtionalFee = 0
    totalcost = surface * pricePerSqft + treeprice + labourFee + addtionalFee
    print("Total cost for house", houseNumber, "is: {0:.2f}".format(totalcost))


houseNumber = int(input("Enter House Number: "))
depthOfLand = float(input("Enter property depth (feet): "))
widthOfLand = float(input("Enter property width (feet): "))
grassKind = str(input("Enter type of grass (fescue, bentgrass, campus): ").lower())
while grassKind != "fescue" and grassKind != "bentgrass" and grassKind != "campus":
    print("You entered an invalid grass type. Please try it again.")
    grassKind = str(input("Enter type of grass (fescue, bentgrass, campus): ").lower())

numberOfTrees = int(input("Enter the number of trees: "))
calculationOfTotalCost(houseNumber, depthOfLand, widthOfLand, grassKind)
