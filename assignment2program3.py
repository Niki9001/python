"""
Name: Niki Xiaoning Zheng
W0470221
Assignment 2 program 3
"""

"""
Step 1: Define insurance calculate rate function.
Step 2: Enter gender, if wrong enter, throw error and let user try it again.
Step 3: If gender is valid type, enter age, if age is invalid, throw error and let user try it again. 
Step 4: If gender and age are valid, enter price of vehicle.
Step 5: Calculate the price of insurance.
Step 6: Output
"""

def insuranceRate(gender,age,vehiclePrice):

    if gender == "male":
        if age >= 15 and age < 25:
            monthlyRate = vehiclePrice * (0.25/12)
        elif age >= 25 and age < 40:
            monthlyRate = vehiclePrice * (0.17/12)
        elif age >= 40 and age < 70:
            monthlyRate = vehiclePrice * (0.1/12)
    elif gender == "female":
        if age >= 15 and age < 25:
            monthlyRate = vehiclePrice * (0.20 / 12)
        elif age >= 25 and age < 40:
            monthlyRate = vehiclePrice * (0.15 / 12)
        elif age >= 40 and age < 70:
            monthlyRate = vehiclePrice * (0.1 / 12)
    print("Your monthly insurance will be: {0:.2f}".format(monthlyRate))

gender = str(input("Are you 'Male' or 'Female': ").lower())
while gender != "male" and gender != "female":
    print("You entered an invalid gender. Please try it again.")
    gender = str(input("Are you 'Male' or 'Female': ").lower())
age = float(input("Enter your age: "))
while age < 15 or age >= 70:
    print("You entered an invalid age. Please try it again.")
    age = float(input("Enter your age: "))
vehiclePrice = float(input("Enter the purchase price of the vehicle: "))
insuranceRate(gender,age,vehiclePrice)