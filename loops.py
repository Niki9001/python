"""
嵌套循环
循环嵌套时，外层循环每执行一次，内层循环要执行一圈。

"""

#打印递增*
i = 6
while i > 0:
    i = i - 1
    a = 0
    while a < i :
        a = a + 1
        print("*",end="")
    print()

#打印递减*
a = 0
while a < 5:
    a = a + 1
    b = 0
    while b < a:
        b = b + 1
        print("*",end="")
    print()


#打印乘法口诀
while i < 9:
    i = i + 1
    j = 0
    while j < i:
        j = j + 1
        #print(f"{j}*{i} ={i * j}",end="\t")
        print("{} * {} =".format(j,i), i*j,end="\t")
    print()
"""
i = 0
while i < 9 控制高度
    a = 0
    while a < i 控制宽度
字符串拼接方式
.format
name = "Niki"
age = 18
height = 180
str1 = "My name is {}. I am {}. My height is {}.".format(name,age,height)
str2 = f"My name is {name}. I am {age}. My height is {height}."
"""
aa = 15
bb = 5
print(f"{aa} * {b} = {aa * b}")
print("{} * {} = ".format(aa,b),aa*b)

#求100以内的质数
i = 2
while i <= 100:
    flag = True
    j = 2
    while j < i:
        if i % j == 0:
            flag = False
        j += 1
    if flag:
        print(i)
    i = i + 1

#求任意数是不是质数
a = int(input("Please input a number over 1: "))
while a <= 1:
    print("Please input again")
    a = int(input("Please input a number over 1: "))
b = 2
flag = True
while b < a:
    if a % b == 0:
        flag = False
    b = b + 1
if flag == True:
    print(f"{a} is True")
else:
    print(f"{a} is not True")

"""
break
    break可以立即退出循环语句（else会一起被退出）
continue
    continue可以用来跳过当次循环
break和continue支队离他最近的循环起作用
pass
    pass是用来在循环中占位
测试程序运行时间
    通过模块可以对python进行扩展
    time模块可以统计程序执行时间
    time()函数可以用来获取当前的时间，返回的单位是秒
    begin = time()
    end = time()
    print(begin - end)
"""