"""

Name: Niki Xiaoning Zheng
StudentNumber: W0470221
Assignment 1
Program 2

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


"""
Program 2 - Weekly Loan Calculator
"""
import math
print("Weekly Loan Calculator")
a = float(input("Enter the amount of loan: "))
r = float(input("Enter the interest rate (%): "))
n = float(input("Enter the number of years: "))
weeklypayment = (r/5200)/(1-math.pow((1+r/5200),(-52*n)))*a
print("Your weekly payment will be: ${0:.2f}".format(weeklypayment))

"""
Program 3 - Imperial to Metric Conversion
"""
print("Imperial To Metric Conversion")
tons = float(input("Enter the number of tons: "))
stone = float(input("Enter the number of stone: "))
pounds = float(input("Enter the number of pounds: "))
ounces = float(input("Enter the number of ounces: "))
totalounces = 35840 * tons + 224 * stone + 16 * pounds + ounces
totalkilos = totalounces / 35.274
metrictons = int(totalkilos/1000)
metrickilos = int(totalkilos-metrictons*1000)
metricgrams = (totalkilos-metrictons*1000-metrickilos)*1000

print("The metric weight is", metrictons,"tons,",metrickilos," kilos, and{0:.1f} ".format(metricgrams),"grams.")