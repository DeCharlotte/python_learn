import time, threading, multiprocessing

"""
多任务可以由多进程完成，也可以由一个进程内的多线程完成。我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。
由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，
    并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程
Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。
    绝大多数情况下，我们只需要使用threading这个高级模块
"""

# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行


def loop():  # 新线程执行的代码
    print('Thread %s is running.' % threading.current_thread().name)  # Thread LoopThread is running.
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))  # thread LoopThread >>> 1
        time.sleep(1)
    print('Thread %s is done.' % threading.current_thread().name)  # Thread LoopThread is done.


print('Thread %s is running.' % threading.current_thread().name)  # Thread MainThread is running.
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('Thread %s is done.' % threading.current_thread().name)  # Thread MainThread is done.

# 由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程

"""
线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了
加锁：threading.Lock()
"""

balance = 0  # 银行存款-全局变量
lock = threading.Lock()


def change_balance(n):
    global balance  # 声明变量在函数中是全局变量，而不是局部变量;没有使用 global 关键字，函数会在局部作用域中创建一个新的变量 balance
    balance += n
    balance -= n


def run_thread(n):
    for i in range(1000000):
        lock.acquire()  # 获取锁
        try:
            change_balance(n)
        finally:
            lock.release()  # 释放锁


t1 = threading.Thread(target=run_thread, args=(5, ))
t2 = threading.Thread(target=run_thread, args=(8, ))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)  # 0

print(multiprocessing.cpu_count())  # 8

"""
Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，
    即使100个线程跑在100核CPU上，也只能用到1个核

Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响
"""
