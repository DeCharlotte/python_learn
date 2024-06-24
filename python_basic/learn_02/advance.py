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

# 迭代：