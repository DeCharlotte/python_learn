# task_worker.py

import time, sys, queue
from multiprocessing.managers import BaseManager

"""
启动任务进程
"""


class QueueManager(BaseManager):
    pass


# 注册，从网络上获取queue
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器(运行task_master.py的机器)
server_address = '127.0.0.1'
print('connect to server %s...', server_address)
# 端口和验证码与task_master.py一致
manager = QueueManager(address=(server_address, 5000), authkey=b'abc')
# 从网络链接
manager.connect()
# 获取Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 从task队列取任务，处理后结果写入result队列中
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('Run task %d * %d' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty.')
# 处理结束
print('worker exit.')

