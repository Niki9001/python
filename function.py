"""
Name: Niki Xiaoning Zheng
W0470221
Function excises 1
Marks

"""
"""
Step 1: Input the mark
Step 2: Processing with conditions
Step 3: Output
"""

c = float(input("Please enter your mark: "))
def mark(a):
    if c < 60:
        return "You fail the exam"
    elif c >= 60 and c < 70:
        return "Your value is : Pass"
    elif c >= 70 and c < 80:
        return "Your value is : Good"
    elif c >= 80 and c < 90:
        return "Your value is : Excellent"
    elif c >= 90 and c <= 100:
        return "Your value is : Perfect"
    else:
        return "Wrong input, please enter again。"
print(mark(c))
