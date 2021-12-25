# coding=utf-8
# '''
# Author: wuxh
# Date: 2021-12-04 21:22:40
# LastEditTime: 2021-12-04 21:22:40
# LastEditors: wuxh
# Description: 
# FilePath: /example/python/基于场景的人工智能综合应用/第一天/练习代码/001.list.py
# '''



import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# 返回多个数值
print(move(10, 10,1)) 
#(11.0, 10.0)
print(move(10, 10,1)[0])
# 11.0


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def myFunction(c, d):
    for num1 in range(c):
        if num1 % 2 == 0 and num1 % 4 == 0:
            print(str(num1) + " is multiple of four") 
        elif num1%2 == 0 and num1 % 4 != 0:
            print(str(num1) + " is even, but not a multiple of four")
        else:
            print(str(num1) + " is odd!")
    print("-" * 10)
    for num2 in range(1, d, 2):
        print(num2, 2 ** num2)

def main():
    a = 5
    b = 10
    myFunction(a, b)
    
# 默认参数
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def power(x, n = 2):
    s = 1
    while n > 0:
        n -=1
        s = s * x
    return  s


# 可变参数，定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 必选参数(a, b)、默认参数(c)、可变参数(args)、关键字参数(kw)和命名关键字参数
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

if __name__ == '__main__':
    main()
    print(power(2, 10))
    f1(1, 2) # a = 1 b = 2 c = 0 args = () kw = {}
    f1(1, 2, c = 3)
    f1(1, 2, 3, 'a', 'b')
    f1(1, 2, 3, 'a', 'b', x = 99)
    f2(1, 2, d=99, ext=None)
    
    
    
    