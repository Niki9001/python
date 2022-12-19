"""
Name : Niki Xiaoning Zheng
No.: w0470221
Topic : The paint shop

"""
import math

print("Welcome to our paint shop")                                      # Welcome sentence
widthofthewall = int(input("The width of your wall (in ft) : "))        # Ask customers width of the wall
heighofthewall = int(input("The height of your wall (in ft): "))        # Ask customers height of the wall
numOfsquare = widthofthewall * heighofthewall                           # Calculate the area of the wall
print("The total area of your wall is", numOfsquare, "sqft.")           # Output the result
gallonpersqft = 150                                                     # Define 1 gallon work area
totalpaintneed = numOfsquare / gallonpersqft                            # Calculate the math answer
print("One gallon can paint 150 sqft, paint is only sold by gallon.")
# In case of the paint sold by gallon, so I use math.ceil to solve this issue.
print("So, the total gallon of paint you need is",
      math.ceil(totalpaintneed), end = "")
# A simple solution for automatically determining vocabulary singular or plural
if totalpaintneed <= 1:
    print(" Gallon.", end = "")
else:
    print(" Gallons.", end = "")
