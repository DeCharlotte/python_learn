from functools import reduce
import logging
logging.basicConfig(level=logging.INFO)   # 记录信息的级别 debug info warning error


"""
在程序运行过程中，总会遇到各种各样的错误;Python内置了一套异常处理机制，来帮助我们进行错误处理。
此外，我们也需要跟踪程序的执行，查看变量的值是否正确，这个过程称为调试
最后，编写测试也很重要。有了良好的测试，就可以在程序修改后反复运行，确保程序输出符合我们编写的测试
"""

# 错误处理:try...except...finally...机制
# Python的错误其实也是class，所有的错误类型都继承自BaseException
try:
    print('try...')
    r = 10 / int('0')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:  # 当没有错误发生时，会自动执行else语句
    print('No Error!')
finally:
    print('finally...')
print('End')


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('a')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')


# try...except捕获错误可以跨越多层调用
main()
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。
# 既然我们能捕获错误,就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去
# Python内置的logging模块可以非常容易地记录错误信息


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('end')  # 程序继续执行

# 错误是class，捕获一个错误就是捕获到该class的一个实例
# Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误
# 抛出错误-raise语句


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('Invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError:', e)  # 捕获错误目的只是记录一下，便于后续追踪;当前函数不知道应该怎么处理该错误
        raise  # raise语句如果不带参数，就会把当前错误原样抛出


def str2num(s):
    try:
        return int(s)
    except ValueError as e:
        pass
    finally:
        return float(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()

""""
调试：
    1.用print打印结果
    2.用assert断言代替print：断言失败，assert语句本身就会抛出AssertionError
        启动Python解释器时可以用-O参数来关闭assert:python -O err.py
    3.用logging代替print:logging不会抛出错误，而且可以输出到文件
    4.使用Python的调试器pdb,让程序以单步方式运行，可以随时查看运行状态:python -m pdb err.py
"""


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('1')


main()  # AssertionError: n is zero!

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


"""
单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作
可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行
"""

"""
文档测试:代码与其他说明可以写在注释中，然后，由一些工具来自动生成文档
    Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试
"""


