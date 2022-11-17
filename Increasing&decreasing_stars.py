#Decreasing *
i = 6
while i > 0:
    i = i - 1
    a = 0
    while a < i :
        a = a + 1
        print("*",end="")
    print()

#Increasing *
a = 0
while a < 5:
    a = a + 1
    b = 0
    while b < a:
        b = b + 1
        print("*",end="")
    print()
# 2nd way to print increasing *
i = 0
for i in range(6):
    for j in range(i):
        print("*",end="")
    print()
print("\n")
