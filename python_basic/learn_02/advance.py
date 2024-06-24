from collections.abc import Iterable
from collections.abc import Iterator
import os  # 导入os模块

"""
Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好
高级特性:切片、迭代、列表生成式、生成器、迭代器
"""

# 切片:取指定索引范围的操作
L = ['Michael', 'Bob', 'Tracy', 'Alice', 'Jack']
print(L[0:3])  # ['Michael', 'Bob', 'Tracy']; L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3
print(L[:3])  # 省略0
print(L[-2:])  # 倒数切片, ['Alice', 'Jack']

l = list(range(100))
print(l[::5])  # 每五个取一个
# tuple切片
print((1, 2, 3, 4, 5)[1:3])  # (2, 3)
print('abcdefg'[2:5])  # 字符串切片, cde
print('abcdefg'[::2])  # aceg
print(L[0:0])  # []
s = 'hello world  '
for char in s[::-1]:  # [::-1]切片创建一个翻转的字符串，逐个遍历
    print(char)


def trim(s):
    l = 0
    r = 0
    n = len(s)
    for i in s:
        if i == ' ':
            l += 1
        else:
            break
    for j in s[::-1]:  # 切片创建一个翻转的字符串，逐个遍历
        if j == ' ':
            r += 1
        else:
            break
    print('l:', l, 'r:', r)
    if l == n:
        return ''
    return s[l:n - r]


print(trim(s), len(trim(s)))  # hello world  11

# 迭代：如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
# 在Python中，迭代是通过for ... in来完成的，而很多语言比如C语言，迭代list是通过下标完成的
d = {'a':1, 'b':2, 'c':3, 'd':4}

for k in d:
    print(k)  # a b c

for v in d.values():
    print(v)  # 1 2 3

for k, v in d.items():
    print(k, v)  # a 1 b 2 c 3

for char in 'ABC':
    print(char)  # A B C

# 判断是否可以迭代
print(isinstance('ABC', Iterable))  # True
print(isinstance([1,2,3], Iterable))  # True

for index, value in enumerate([1, 2, 3, 4, 5]):   # enumerate函数可以把一个list变成索引-元素对
    print(index, value)  # (索引,元素） (0,1) (1,2) ...

for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)  # 1 2   3 4   5 6

# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
# 生成[1,2,3,4,5,6,7,8,9,10]
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 生成[1*1, 2*2, ...]
# L = []
# for i in range(1, 11):
#     L.append(i * i)
L = [x * x for x in range(1, 11)]
L = [x * x for x in range(1, 11) if x % 2 == 0]  # 加上过滤条件
s = [m + n for m in 'ABC' for n in 'XYZ']  # 两层for循环

print([d for d in os.listdir('.')])  # ['advance.py', 'function.py']
d = {'a':1, 'b':2, 'c':3, 'd':4}
L = [k + '=' + str(v) for k, v in d.items()]  # ['a=1', 'b=2', 'c=3', 'd=4']

L = ['Hello', 'World', 'Python']
print([x.lower() for x in L])  # ['hello', 'world', 'python']

"""
跟在for后面的if是一个筛选条件，不能带else;for前面的部分是一个表达式，它必须根据x计算出一个结果,必须带else
"""
print([x for x in range(1, 11) if x % 2 == 0])  # [2, 4, 6, 8, 10]
print([x if x % 2 == 0 else 0 for x in range(1, 11)])  # [0, 2, 0, 4, 0, 6, 0, 8, 0, 10]

# 生成器：在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x * x for x in range(1, 11)]
g = (x * x for x in range(1, 11))  # <generator object <genexpr> at 0x00000260868B8110>
# 打印generator:generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
for i in g:
    print(i)

# generator用类似列表生成式的for循环无法实现的时候，还可以用函数来实现
# 斐波拉契数列:1 1 2 3 5 8 13...


def fib(n):
    m, a, b = 1, 0, 1
    while m <= n:
        print(b)
        a, b = b, a + b
        m += 1
    return 'done'


fib(5)  # 1 1 2 3 5

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator函数，
# 调用一个generator函数将返回一个generator


def fib2(n):
    m, a, b = 1, 0, 1
    while m <= n:
        yield b  #
        a, b = b, a + b
        m += 1
    return 'done'


# generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
print(fib2(6))  # <generator object fib2 at 0x0000021C46B4DE00>
g = fib2(6)
for i in g:
    print(i)  # 1 1 2 3 5 8

# 用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，
# 必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib2(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 定义一个generator:计算杨辉三角


def triangles():
    a, b = [1], [1, 1]
    yield a
    yield b
    while True:
        x = [1]
        for index, value in enumerate(b):
            if 0 < index < len(b):
                x.append(b[index - 1] + b[index])
        x.append(1)
        b = x
        yield b


def triangles2():
    row = [1]
    while True:
        yield row
        row = [1] + [row[i] + row[i + 1] for i in range(0, len(row) - 1)] + [1]


n = 0
results = []
for t in triangles2():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

"""
直接作用于for循环的数据类型有以下几种：
    一类是集合数据类型，如list、tuple、dict、set、str等；
    一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
"""

# 使用isinstance()判断一个对象是否属于Iterable对象
print(isinstance([], Iterable))  # True
print(isinstance((), Iterable))  # True
print(isinstance({}, Iterable))  # True
print(isinstance('', Iterable))  # True
print(isinstance((x for x in range(10)), Iterable))  # True
print(isinstance(100, Iterable))  # False

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 使用isinstance()判断一个对象是否是Iterator对象
print(isinstance('', Iterator))  # False
print(isinstance((), Iterator))  # False
print(isinstance([], Iterator))  # False
print(isinstance({}, Iterator))  # False
print(isinstance((x for x in range(10)), Iterator))  # True

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]), Iterator))  # True

"""
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
Python的for循环本质上就是通过不断调用next()函数实现的
"""