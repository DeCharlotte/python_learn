"""
Python不但能非常灵活地定义函数，而且本身内置了很多有用的函数，可以直接调用
"""
import math

# 调用函数
print(abs(-2))  # 2
print(max(1, 2, -7, 4, 0, 8))  # 8
# int():把其它类型的数据转化为整型  float() str() double() bool() hex()
print(int('123'))  # 123
print(int(12.34))  # 12
print(str(1.23))  # '1.23'
# 函数名是对于函数的引用
a = abs  # 变量a指向abs函数
print(a(-34))  # 34

"""
在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
然后，在缩进块中编写函数体，函数的返回值用return语句返回
如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return
"""


def my_abs(x):
    # 对参数类型做检查，只允许整数和浮点数类型的参数
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print('my_abs(-2) = ', my_abs(-2))  # 2
# 如果想定义一个什么事也不做的空函数，可以用pass语句
# pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来


def nop():
    pass


# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


r = move(100, 200, 10, 180)
print(r)  # (94.01539930942141, 191.9884736426617) -tuple
x, y = move(100, 200, 10, 180)
print(x, y)  # 94.01539930942141 191.9884736426617

"""
定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，
只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解
默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码
"""


# 位置参数
def pow(x, n=2):  # 默认参数n=2  必选参数在前，默认参数在后
    ans = 1
    while n > 0:
        n = n - 1
        ans = ans * x
    return ans


print(pow(2, 6))  # 64
print(pow(2))  # 4


def add_end(l=[]):  # Default argument value is mutable
    l.append('END')
    return l


# 默认参数必须指向不变对象
print(add_end())  # ['END']
print(add_end())  # ['END', 'END']
print(add_end())  # ['END', 'END', 'END']
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了


def add_end1(l=None):
    if l is None:
        l = list()
    l.append('END')
    return l


print(add_end1())  # ['END']
print(add_end1())  # ['END']
print(add_end1())  # ['END']

# 可变参数  可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
# 计算 a^2 + b^2 + c^2 + ...


def calc(numbers):
    sum = 0
    for i in numbers:
        sum += i * i
    return sum


# 传入list或tuple
print(calc([1, 2, 3]))  # 14
print(calc((1, 2, 3, 4)))  # 30


def calc2(*numbers):  # 可变参数，函数内部，参数numbers接收到的是一个tuple
    sum = 0
    for i in numbers:
        sum += i * i
    return sum


print(calc2(1, 2, 3))  # 14
print(calc2(1, 2, 3, 4))  # 30
nums = [1, 2, 3]
print(calc2(*nums))  # 将list[]转变为可变参数 14

# 关键字参数  关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict


def person(name, age, **kwds):
    print('name:', name, 'age:', age, 'other:', kwds)

person('tom', 12)  # name: tom age: 12 other: {}
person('tom', 24, city='San Francisco', job='Engineer')  # name: tom age: 24 other: {'city': 'San Francisco', 'job': 'Engineer'}


extra = {'city': 'San Francisco', 'job': 'Engineer'}
person('tom', 22, **extra)
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

# 命名关键字参数
# 关键字参数，函数的调用者可以传入任意不受限制的关键字参数,限制关键字参数的名字，就可以用命名关键字参数


def person2(name, age, *, city, job):  # 特殊分隔符*后面的参数被视为命名关键字参数
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)


# person2('Alice', 21, 'Beijing', 'no')  # 命名关键字参数必须传入参数名city='San Francisco', job='Engineer'
person2('Bob', 46, city='San Francisco', job='Engineer')  # name: Bob age: 46 city: San Francisco job: Engineer


def person3(name, age, *args, city, job):  # 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
    print('name:', name, 'age:', age, 'args:', args, 'city:', city, 'job:', job)


person3('Jack', 22, *nums, city='San Francisco', job='Engineer')  # name: Jack age: 22 args: (1, 2, 3) city: San Francisco job: Engineer

"""
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
"""


def f1(a, b, c=0, *args, **kwds):
    print('a:', a, 'b:', b, 'c:', c, 'args:', args, 'kwds:', kwds)


def f2(a, b, c=0, *, d, **kwds):
    print('a:', a, 'b:', b, 'c:', c, 'd:', d, 'kwargs:', kwds)


f1(1, 2)  # a: 1 b: 2 c: 0 args: () kwds: {}
f1(1, 2, 3)  # a: 1 b: 2 c: 3 args: () kwds: {}
f1(1, 2, 3, 'a', 'b')  # a: 1 b: 2 c: 3 args: ('a', 'b') kwds: {}
f1(1, 2, 3, 'a', 'b', x=99)  # a: 1 b: 2 c: 3 args: ('a', 'b') kwds: {'x': 99}
f2(1, 2, d=3, ext=None)  # a: 1 b: 2 c: 0 d: 3 kwargs: {'ext': None}
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
args = (1, 2, 3, 4)
kw = {'x': 99, 'y': 99}
f1(*args, **kw)  # a: 1 b: 2 c: 3 args: (4,) kwds: {'x': 99, 'y': 99}
args = (1, 2, 3)
kw = {'d': 88, 'x': 99}
f2(*args, **kw)  # a: 1 b: 2 c: 3 d: 88 kwargs: {'x': 99}

""""
在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数
"""

# 计算阶乘 n!


def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))  # 120
# print(fact(1000))  # RecursionError: maximum recursion depth exceeded

# 解决栈溢出：尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况


def fact2(n):
    return fact_iter(n, 1)


def fact_iter(n, product):
    if n == 1:
        return product
    else:
        return fact_iter(n - 1, n * product)  # num - 1和num * product在函数调用前就会被计算，不影响函数调用


# print(fact2(1000))
