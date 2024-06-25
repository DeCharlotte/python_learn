
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

    return reduce(lambda x, y : x * 10 + y, map(char2num, s))


print(str2num2('123'))  # 123

print('HELLO'.lower())

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456


def str2float(s):
    # map():将单个字符转化为单个数字; reduce():将这些数字组成float
    integer_part, decimal_part = s.split('.')  # 将s划分为整数部分和小数部分
    def char2num(c):
        digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        return digits[c]

    return reduce(lambda x, y : x * 10 + y, map(char2num, integer_part)) + reduce(lambda x, y : x * 10 + y, map(char2num, decimal_part)) / (10 ** len(decimal_part))


print(str2float('123.456'))  # 123.456

# 高阶函数2、filter():Python内建的filter()函数用于过滤序列。
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素;filter()函数返回的是一个Iterator，也就是一个惰性序列


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, range(10))))  # 筛选奇数,[1, 3, 5, 7, 9]


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', ' ', 'B', None, '', '  ', 'C'])))  # ['A', 'B', 'C']

# 用filter求素数-埃式筛法


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n  # 生成器，构造从3开始的奇数序列


def _not_divisible(n):  # 筛选函数，
    return lambda x : x % n > 0


def prime():
    yield 2
    it = _odd_iter()  # 初始化序列
    while True:
        n = next(it)  # 获取序列的第一个值
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印100以内的素数
for n in prime():
    if n < 100:
        print(n)
    else:
        break


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数


def is_palindrome(n):
    n = str(n)  # int -> str
    l, r = 0, len(n) - 1
    while l < r:
        if n[l] != n[r]:
            return False
        l += 1
        r -= 1
    return True


def is_palindrome2(n):
    n = str(n)
    return n == n[::-1]


# 测试:
output = filter(is_palindrome2, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome2, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

# 排序函数-sorted()  比较数字、字符、dict

print(sorted([10, 2, -8, 100, 0]))  # [-8, 0, 2, 10, 100]
print(sorted(['about', 'Zoo', 'by', 'Create']))  # 按照ASCII大小：['Create', 'Zoo', 'about', 'by']
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
print(sorted([10, 2, -8, 100, 0], key=abs))  # 按照绝对值排序; [0, 2, -8, 10, 100]
print(sorted(['about', 'Zoo', 'by', 'Create'], key=str.lower))  # 不区分大小写排序;['about', 'by', 'Create', 'Zoo']
print(sorted(['about', 'Zoo', 'by', 'Create'], key=str.lower, reverse=True))  # 反向排序

"""
返回函数：高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
"""

# 可变参数求和


def calc_sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(calc_sum(1, 2, 3, 4, 5, 6))  # 21
# 如果不需要立即计算和,而是在后续的代码中在计算,能不能不但会求和的结果，而是将求和函数作为返回值


def lazy_sum(*args):
    def calc_sum():
        sum = 0
        for i in args:
            sum += i
        return sum

    return calc_sum


print(lazy_sum(1, 2, 3, 4, 5, 6))  # <function lazy_sum.<locals>.calc_sum at 0x000001E28B835120>
print(lazy_sum(1, 2, 3, 4, 5, 6)())  # 21
print(lazy_sum(1, 2, 3, 4) == lazy_sum(1, 2, 3, 4))  # False 每次会产生新的函数

# 闭包（Closure）：相关参数和变量都保存在返回的函数中


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


f1, f2 , f3 = count()
print(f1(), f2(), f3())  # 9 9 9  返回的函数并没有立刻执行，而是直到调用了f()才执行，而引用的变量i均变为了3
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量


def count_2():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2 , f3 = count_2()
print(f1(), f2(), f3())  # 1 4 9 用f绑定外界的局部变量i,使得计算的g函数使用f绑定的不同值

# 使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量


def inc():
    x = 0
    def fn():
        return x + 1  # 只读外层函数的局部变量x

    return fn


def inc_2():
    x = 0
    def fn():
        nonlocal x  # 加上此此句，python解释器会将x当作外层函数的局部变量
        x = x + 1
        return x
    return fn

