import os, time, random, subprocess
from multiprocessing import Process, Pool, Queue

"""
线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。
多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂

Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
    因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，
    而子进程只需要调用getppid()就可以拿到父进程的ID

Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程
"""

# print('Process (%s) start' % os.getpid())
# pid = os.fork()  # AttributeError: module 'os' has no attribute 'fork'
# if pid == 0:
#     print('I\'m child process (%s) and I\'m parent process is (%s)' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) create a process (%s)' % (os.getpid(), pid))

"""
由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序？
由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
multiprocessing模块提供了一个Process类来代表一个进程对象
"""


def run_func(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s start' % os.getpid())  # Parent process 3852 start
    p = Process(target=run_func, args=('test',))
    print('Child process will start')
    p.start()  # Run child process test (11820)
    p.join()
    print('Child process end')

# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程


def long_time_task(name):
    print('Task %s (%s) run' % (name, os.getpid()))  # Task 0 (3020) run
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %0.2f seconds' % (name, end - start))  # Task 1 run 0.01 seconds


if __name__ == '__main__':
    print('Parent process %s start' % os.getpid())  # Parent process 18144 start
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocess done...')
    p.close()  # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    p.join()  # Pool对象调用join()方法会等待所有子进程执行完毕
    print('All subprocess done')


# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出
# 如何在Python代码中运行命令nslookup www.python.org
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

"""
进程间通信:
    Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
    Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据
"""

# 在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据


def write(q):  # 写进程执行的代码
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random() * 3)


def read(q):  # 写进程执行的代码
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue...' % value)


if __name__ == '__main__':
    q = Queue()  # 父进程创建Queue，并传给两个子进程
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()  # 启动读进程，写入  Process to write: 10840
    pr.start()  # 启动写进程，读入  Process to read: 3704
    pw.join()
    pr.terminate()  # 死循环，强制结束


