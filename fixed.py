"""
Write a program that takes two pieces of input data
 a pay rate per hour and the number of hours worked ,
  and output the total pay.
  Any hours over 40 are paid at time and a half.

"""

"""
Fix this program and submit to me on Friday. 
"""

# Input
totalHours = float(input("Enter number of hours: "))
hourlyRate = float(input("the hourly wage: "))
# Processing:
#totalPaid = totalHours*hourlyRate
overTime = 0
if totalHours > 40:
    overTime = totalHours-40
    #totalPaid = 40*hourlyRate + overTime*1.5*hourlyRate
totalPaid = 40*hourlyRate + overTime*hourlyRate*1.5
# Output
print ("The total payment is : $ {0:.2f}".format(totalPaid))