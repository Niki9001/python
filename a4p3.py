"""
Name: Niki Xiaoning Zheng
W0470221
Assignment 4 Program 3
"""
"""
This is the method to write this program.

Step 1: Input limitation number
Step 2: Use for loop to input data
Step 3: Use loop to output list
Step 4: Simple calculate
Step 5: Zip student name list and python course list as a 2d list
Step 6: Traversal the entire 2d list and find element meet requirement, pick them up with name
Step 7: Zip student name list and database course list as a 2d list 
Step 8: Traversal the entire 2d list and find element meet requirement, pick them up with name
Step 9: Output the list which in student name and use sort output again.
"""



numOfSt = int(input("How many number of students: "))
print(f"Enter student name and marks for the {numOfSt} students")
# make list storage elements which input by uses
StName = [] # This is a student name list
Py_course = [] # This is a python course mark list
Data_BaseCourse = [] # This is a database course mark list
for i in range (numOfSt): # Ust loop let user input
    i = i + 1 # Control the loop length
    stName = str(input(f"Enter student's name #{i}      :")) # Input data
    pyMark = float(input(f"Enter {stName}'s mark in python: ")) # Input data
    dbMark = float(input(f"Enter {stName}'s mark in DB    : ")) # Input data
    StName.append(stName) # Append input result into list
    Py_course.append(pyMark) # Append input result into list
    Data_BaseCourse.append(dbMark) # Append input result into list
print("--------------------------------------------------")
print("StName   Python Course  Data BaseCourse")
print("------   -------------  ---------------")
for i in range(len(StName)):
    print("  %-10s %-16s %-20s"%(
        StName[i],Py_course[i],Data_BaseCourse[i]
    )
          ) # use %s occupy space and output the list content
print("--------------------------------------------------")
sPyC = sum(Py_course)       # python course mark sum
sDbC = sum(Data_BaseCourse) # Database course mark sum
aPyC = sPyC/numOfSt         # Python average mark
aDbC = float(sDbC/numOfSt)  # Database average mark
print(f"The total mark of python Course is : {sPyC}, and Data Base course is: {sDbC}")
print(f"The average mark of python Course is : {aPyC}, and Data Base course is: {aDbC}")
print("----------------The First Report------------------")
print("Students' Marks less than Average in DB courses") #  Here is the part display students' mark less than avg
matr = list(zip(StName,Data_BaseCourse)) # Zip StName list and Data_BaseCourse list become a 2d list
for name,low_score in matr: # Use loop to search entire 2d list
    if low_score < aDbC: # If met element meet requirement
        print(f"{name} got {low_score} for Data Base Course") # Pick up the entire row in the 2d list.
print("----------------The Second Report-----------------")
print("Students' Marks who were suppoerted in Python Course") # This part display student fail the exam
matri = list(zip(StName,Py_course)) # Zip StName list and Py_course list become a 2d list
for name2,failscore in matri: # Use loop to search entire 2d list
    if failscore < 60: # If element meet requirement
        print(f"{name2} got {failscore+5} in Python") # Pick up the entire row in the 2d list and add 5 marks
print("----------------The Second Report-----------------")
print("Students' name before sorted in ascending order")
print(StName) # Output student name by input order
print("Students' name after sorted in ascending order")
print(sorted(StName)) #Output student name by ascending order