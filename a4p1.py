"""
Name: Niki Xiaoning Zheng
w0470221
Assignment 4 Program 1
"""

def calculate(deHours):
    hoursnDayList = []
    imax = 0

    for i in range(0, 5):
        i = i + 1
        hours = int(input(f"Enter hours worked on Day #{i}: "))
        if hours > imax:
            imax = hours

        hoursnDayList.append(hours)
    sumHours = sum(hoursnDayList)
    avgHours = sumHours / i
    print("---------------------------------------------------")
    print("The most hours worked was on:")
    for listNum, mhours in enumerate(hoursnDayList):
        if mhours == imax:
            print(f"Day #{listNum + 1} when you worked {mhours} hours")
    print("---------------------------------------------------")
    print(f"The total number of hours workd was: {sumHours}")
    print(f"The average number of hours worked each day was: {avgHours}")
    print("---------------------------------------------------")
    print(f"Days you slacked off (i.e. worked less than {deHours} hours):")
    for listNum2, lHours in enumerate(hoursnDayList):
        if lHours < deHours:
            print(f"Day #{listNum2 + 1}: {lHours} hours")
calculate(7)
