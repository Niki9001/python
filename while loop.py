"""
100 以内奇数和
"""

i = 1
r = 0
while i < 100:
    if i % 2 == 1:
        r = r + i
    i = i + 1
print(r)


"""
100以内7的倍数和
"""
i = 7
r = 0
a = 0
while i < 100:
    if i % 7 == 0:
        r = r + i
        a = a + 1
    i = i + 1
print(r,a)