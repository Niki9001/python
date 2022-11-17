"""

Name: Niki Xiaoning Zheng

"""
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
