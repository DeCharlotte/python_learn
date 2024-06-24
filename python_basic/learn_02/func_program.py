
from functools import reduce

"""
函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，
这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元

函数式编程(Functional Programming)就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，
因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，
由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。
函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言
"""

# 高阶函数-Higher-order function
# 1、变量可以指向函数
print(abs(-10))  # 10
print(abs)  # <built-in function abs>
a = abs(-10)
print(a)  # 10
b = abs  # 变量指向函数
print(b)  # <built-in function abs>
print(b(-10))  # 10

# 2、函数名也是变量-函数名其实就是指向函数的变量,如abs()函数,abs就是指向函数的变量
# abs = 10  # abs指向整数对象,不再指向绝对值函数
# print(abs(-10))  # TypeError: 'int' object is not callable
# 由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，
# 要用import builtins; builtins.abs = 10

# 传入函数:变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数


def add(a, b, f):
    return f(a) + f(b)


print(add(-10, 20, abs))  # 30

# 编写高阶函数，就是让函数的参数能够接收别的函数
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式

# 高阶函数1、map()/reduce()
# map():接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# 把函数作用到Iterable,如[1,2,3]的每一个元素上


def f(x):
    return x * x


r = map(f, [x for x in range(10)])  # 在[0,1,...,9]上每个元素运用f(),结果返回Iterator
print(r)  # <map object at 0x000001AC8030FFD0>
print(list(r))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(list(map(str, range(10))))  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# reduce():把一个函数作用在一个序列[x1, x2, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


def add(x, y):
    return x + y


print(reduce(add, range(10)))  # 45

# [1, 3, 5, 7, 9] -> 13579


def f(x, y):
    return x * 10 + y


print(reduce(f, [1, 3, 5, 7, 9]))  # 13579

# str -> int  '123' -> 123
# '123' -> [1,2,3]


def char2num(s):
    digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    return digits[s]


print(reduce(f, map(char2num, '123')))  # 123

DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}


def str2num(s):
    def f(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(f, map(char2num, s))


print(str2num('123'))  # 123


def str2num2(s):
    def char2num(s):
        return DIGITS[s]

    return reduce(lambda x, y: x* 10 + y, map(char2num, s))


print(str2num2('123'))  # 123

print('HELLO'.lower())
