from enum import Enum, unique

"""
在Python中，面向对象还有很多高级特性，允许我们写出非常强大的功能:多重继承、定制类、元类等概念
"""


# __slots__属性:限制该class实例能添加的属性


class Student(object):
    __slots__ = ('name', 'age')  # 只允许添加属性name和age


s = Student()
s.name = 'tom'
s.age = 18
# s.score = 99  # AttributeError: 'Student' object has no attribute 'score'
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的


class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 99
# 在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__

# @property:装饰器,负责把一个方法变成属性调用的
# 既能检查参数，又可以用类似属性这样简单的方式来访问类的变量


class Student2(object):
    @property  # 用于定义 getter 方法，即访问器,使得一个getter方法变成属性,通过访问属性的方式调用该方法
    def score(self):
        return self._score

    @score.setter  # 用于定义 setter 方法,负责把一个setter方法变成属性赋值
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('value must be an integer')
        if value < 0 or value > 100:
            raise ValueError('value must be between 0 and 100')
        self._score = value


s = Student2()
s.score = 99  # 实际为s.set_score(99)
print(s.score)  # 99 实际转化为s.get_score()
# s.score = 101  # ValueError: value must be between 0 and 100

# 定义只读属性:只定义getter方法，不定义setter方法

# 属性的方法名不要和实例变量重名:会造成无限递归，最终导致栈溢出报错RecursionError

"""
多重继承:一个子类就可以同时获得多个父类的所有功能
MixIn设计:在设计类的继承关系时，通常，主线都是单一继承下来的，但是，如果需要“混入”额外的功能，通过多重继承就可以实现.
MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系
"""

class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


# 定制类:形如__xxx__的变量或者函数名有特殊用途，可以帮助我们定制类


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


# 定义一个__str__():返回好看的字符串,易看出实例内部重要的数据
print(Student('tom'))  # Student object (name: tom)

# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化变量a,b

    def __iter__(self):
        return self  # 实例本身就是迭代对象

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10:
            raise StopIteration
        return self.a  # 返回下一个值


fib = Fib()
for i in fib:
    print(i)  # 1 1 2 3 5 8

# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行;不能使用下标取出元素
# print(Fib()[5])  # TypeError: 'Fib' object is not subscriptable
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法


class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a


print(Fib()[0], Fib()[1], Fib()[2])  # 1 1 2

# 切片对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice


class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for _ in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start, stop = n.start, n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for i in range(stop):
                if i > start:
                    L.append(a)
                a, b = b, a + b
            return L


print(Fib()[:3])  # [1, 2]

# 没有对step参数处理，也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的

# 正常情况下，调用不存在的属性会报错;Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性


class Student(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


s = Student('tom')
print(s.name)  # tom
# 调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
print(s.score)  # 99
# print(s.abc)  # None __getattr__()的默认返回是None


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, attr):
        return Chain('%s/%s' % (self._path, attr))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)  # 链式调用 /status/user/timeline/list

# __call__():任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s' % self.name)


s = Student('tom')
s()  # My name is tom
# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样；
# 所以完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别
# 怎么判断一个变量是对象还是函数：需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
print(callable(Student('jerry')))  # True
print(callable(abs))  # True
print(callable('abc'))  # False

"""
定义常量：
    1.大写变量,通过整数来定义;缺点是类型是int，并且仍然是变量
    2.通过枚举类Enum:为这样的枚举类型定义一个class类型，每个常量都是class的一个唯一实例
        Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较
"""

# 获得Month枚举类
Month = Enum('Month', ('January', 'February', 'March', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))
print(Month.January)  # Month.January
for month, member in Month.__members__.items():
    print(month, '=>', member, ',', member.value)  # value属性则是自动赋给成员的int常量，默认从1开始计数。


@unique  # 装饰器：检查保证没有重复
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Mon)  # Weekday.Mon 根据名
print(Weekday['Tue'])  # Weekday.Tue 根据名
print(Weekday(1))  # Weekday.Mon 根据value
print(Weekday.Fri.value)  # 5
for day, member in Weekday.__members__.items():
    print(day, '=>', member)

"""
元类(metaclass):当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例
    如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类
    先定义metaclass，就可以创建类，最后创建实例
    metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”
"""

# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
# class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
# type()函数既可以返回一个对象的类型，又可以创建出新的类型
"""
要创建一个class对象，type()函数依次传入3个参数：
    class的名称；
    继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
    仅仅是扫描一下class定义的语法，然后调用type()函数创建出class
"""


def fn(self, name='World'):  # 先定义函数
    print('Hello, %s!' % name)


Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello clas
h = Hello()
h.hello()  # Hello, World!
print(type(Hello))  # <class 'type'>


