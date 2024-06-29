import threading

"""
多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，
    不会影响其他线程，而全局变量的修改必须加锁。但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦
ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
    这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源
一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
    ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题
"""

global_dict = {}
local_school = threading.local()  # ThreadLocal，不用查找dict，ThreadLocal帮你自动做这件事


class Student(object):
    def __init__(self, name):
        self.name = name


def do_task_1():
    # std = global_dict[threading.current_thread()]  # 不传入std，而是根据当前线程查找
    std = local_school.student
    print('Hello %s in (%s)' % (std.name, threading.current_thread().name))


def do_task_2():
    # std = global_dict[threading.current_thread()]
    std = local_school.student
    print('Hello %s in (%s)' % (std.name, threading.current_thread().name))


def std_process(name):
    std = Student(name)
    # global_dict[threading.current_thread()] = std  # 把std放在全局变量global_dict中
    local_school.student = std  # 把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量
    do_task_1()
    do_task_2()


t1 = threading.Thread(target=std_process, args=('tom',), name='t1')
t2 = threading.Thread(target=std_process, args=('jerry',), name='t2')
t1.start()
t2.start()
t1.join()
t2.join()

