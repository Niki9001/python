"""

Name: Niki Xiaoning Zheng
StudentNumber: W0470221
Assignment 1
Program 1

"""


"""
Program 1 - Hipster's Local Vinyl Records

"""
print("Hipster's local Vinyl Records - Customer Order Details ")
customerName = input("Enter the customer's name: ")
distance = float(input("Enter the distance in kilometers for delivery: "))
originalPrice = float(input("Enter the cost of records purchased: "))
print("Purchase summary for", customerName)
deliverCost = distance * 15
purchaseCost = originalPrice * 1.14
print("Delivery Cost:: ${0:.2f}".format(deliverCost))
print("Purchase Cost: ${0:.2f}" .format(purchaseCost))
print("Total cost: ${0:.2f}".format(deliverCost+purchaseCost))