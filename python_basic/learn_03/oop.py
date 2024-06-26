"""
面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，
    一个对象包含了数据和操作数据的函数
在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
"""


class Student(object):  # 类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
    # self就指向创建的实例本身;有__init__方法，创建实例的时候，不能传入空的参数了，必须传入与__init__方法匹配的参数
    def __init__(self, name, score):  # 在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去
        self.__name = name  # private变量以__开头
        self.__score = score

    def print_score(self):  # 与普通函数相比，只是第一个参数为self,且调用时不用传self
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


tom = Student('Tom Simpson', 89)
jack = Student('Jack Curry', 99)
tom.print_score()  # Tom Simpson: 89
print(tom.get_grade())  # B
jack.print_score()  # Jack Curry: 99
print(jack.get_grade())  # A
# 实例变量可以指向任何对象
# tom.age = 8 在 tom 实例上动态创建了一个新的属性 age;不是类 Student 定义的一部分;实例属性，只属于特定实例
tom.age = 8
print(tom.age)  # 8
# 通过__dict__查看实例的属性字典
print(tom.__dict__)  # {'name': 'Tom Simpson', 'score': 89, 'age': 8}
# print(jack.age) # AttributeError: 'Student' object has no attribute 'age'
print(jack.__dict__)  # {'name': 'Jack Curry', 'score': 99}

# 访问限制:在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
# print(tom.__name)  # AttributeError: 'Student' object has no attribute '__name'
# 类中增加get,set方法对内部属性进行操作

# 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
# 以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的;但按照约定，不要直接访问
# 双下划线开头的也不是不能在外部访问；不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name
print(tom._Student__name)  # Tom Simpson

"""
继承：定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
    而被继承的class称为基类、父类或超类（Base class、Super class）
"""


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):  # 覆盖/重写
        print('Dog is running...')
    def eat(self):
        print('Dog eats meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')
    def eat(self):
        print('Cat eats fish...')


dog = Dog()
dog.run()  # Dog is running...
cat = Cat()
cat.run()  # Cat is running...

# 定义一个class时，实际上就定义了一种数据类型。我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样
a = list()
b = Animal()
c = Dog()
print(isinstance(a, list))  # True
print(isinstance(b, Animal))  # True
print(isinstance(c, Dog))  # True
print(isinstance(c, Animal))  # True 子类可以被看作父类


def run_twice(animal):  # 传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法-多态
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())


class Timer(object):
    def run(self):
        print('Start...')


# 动态语言-"鸭子模型":不要求严格的继承体系,只需要保证传入的对象有一个run()方法就可
run_twice(Timer())  # Start... \n Start...
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的

# 获取对象信息:获取对象是什么类型、有哪些方法
# 获取对象类型-type()
print(type(123))  # <class 'int'>
print(type('123'))  # <class 'str'>
print(type([]))  # <class 'list'>
print(type(abs))  # <class 'builtin_function_or_method'>
print(type(b))  # <class '__main__.Animal'>

# 判断继承关系-isinstance()

# 获取一个对象的所有属性和方法-dir()

