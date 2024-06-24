'''
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
'''
from unittest import case

# elif = else if
age = int(input('input your age: '))  # input返回的数据类型是str, int()将str转化为int
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

'''
用if ... elif ... elif ... else ...判断时，会写很长一串代码，可读性较差。
如果要针对某个变量匹配若干种情况，可以使用match语句 - 模式匹配
使用match语句时，我们依次用case xxx匹配，并且可以在最后（且仅能在最后）加一个case _表示“任意值”
'''
score = 'B'
match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _:  # _表示匹配到其他任何情况
        print('score is unknown.')

# 复杂匹配
# match语句除了可以匹配简单的单个值外，还可以匹配多个值、匹配一定范围，并且把匹配后的值绑定到变量
match age:
    case x if x < 10:  # 表示age < 10 成立，并赋值给变量x
        print(f'{x} is less than 10')
    case 10:  # 匹配单个值
        print("10 years ols")
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 :  # 匹配多个值
        print("11~18 years ols")
    case _:
        print('not sure')

# 匹配列表
# 用匹配解析列表
args = ['gcc', 'hello.c', 'word.c']
# args = ['clean']
# args = ['gcc']
match args:
    # 如果仅出现gcc, 报错：
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc, 且至少指定了一个文件
    # 列表第一个字符串是'gcc'，第二个字符串绑定到变量file1，后面的任意个字符串绑定到*files
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + '.' + '.'.join(files))
    # 仅出现clean
    case [clean]:
        print('clean')
    case _:
        print('invalid command')