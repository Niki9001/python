"""
Prime numbers under 100
Author: Niki Zheng
"""

"""
Input
"""
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

"""
Output
"""
