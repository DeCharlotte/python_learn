# task_master.py

import random, time, queue
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager

"""
如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，希望把发送任务的进程
    和处理任务的进程分布到两台机器上。怎么用分布式进程实现?
原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue

服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务
"""


# 顶层函数，用于返回全局的 task_queue
def get_task_queue():
    global task_queue
    return task_queue


# 顶层函数，用于返回全局的 result_queue
def get_result_queue():
    global result_queue
    return result_queue


task_queue = queue.Queue()  # 发送人物的queue
result_queue = queue.Queue()  # 接受结果的queue


class QueueManager(BaseManager):  # 继承BaseManager的QueueManager
    pass


# 注册两个queue到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=get_task_queue)
QueueManager.register('get_result_queue', callable=get_result_queue)
if __name__ == '__main__':
    # Windows下多进程可能出现问题，添加以下代码可以缓解
    freeze_support()
    # 绑定端口5000，设置验证码 'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue
    manager.start()
    # 获得通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %s...' % n)
        task.put(n)
    # 从result队列读取结果
    for i in range(10):
        r = result.get(timeout=10)
        print('Get result %s...' % r)
    # 关闭
    manager.shutdown()
    print('manager exit.')
