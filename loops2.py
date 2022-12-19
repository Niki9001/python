print("Welcome")
print("Plese select:\n 1.Tang \n 2.White")
a = int(input("Please select(1-2):"))
if a == 1:
    print("Welcome Tang.")
elif a == 2:
    print("Still Tang.")
else:
    print("You are Tang again.")
b = 2
c = 2
print(f"Your name is Tang, your attack is {b},your life is {c}")
print("Please select what do you want to do: \n 1. practise \n 2. battle \n 3. run away")
e = 100
d = input("Please select (1-3):".lower())
if d == "exit":
    print("Thanks")

while d == 1:
    b = b + 2
    print(f"Your name is Tang, your attack is {b},your life is {c}, White's life is {e}")
    d = input("Please select (1-3):".lower())
        if b == 100:
            print("Thanks")
            break
while d == 2:
    e = e - 2
    print(f"Your name is Tang, your attack is {b},your life is {c}, White's life is {e}")
    d = int(input("Please select (1-3):".lower()))
    if e == 0:
        print("Thanks")
        break
while d == 3:
    c = c + 2
    if c == 100:
        print("Thanks")
        break
    print(f"Your name is Tang, your attack is {b},your life is {c}, White's life is {e}")
    d = int(input("Please select (1-3):".lower()))
    #while d != 1 or d != 2 or d != 3 or d != "Exit":
        #f = int(input("Please try it again, select (1-3):"))
