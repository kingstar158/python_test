#_*_coding= utf-8_*_
'''
Created on 2016-6-28

@author: kjh
'''
import Queue
from multiprocessing.managers import BaseManager
import random


#发送任务的队列
task_manager = Queue.Queue()

#接受结果的队列
result_manager = Queue.Queue()

class QueueManager(BaseManager):
    pass


#把两个队列都注册到网络上， Callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda: task_manager)
QueueManager.register('get_result_queue', callable=lambda: result_manager)

#绑定端口，设置验证码
manager = QueueManager(address = ('', 5000), authkey = 'abc')

#启动queue
#manager.start()

server = manager.get_server()
server.serve_forever()

#获得通过网络访问的queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

#放几个任务进去
for i in range(10):
    n = random.randint(0, 1000)
    print('Put task %d...' % n)
    task.put(n)
    
#从result里面取出任务
print 'Try  get result...'
for i in range(10):
    r = result.get(timeout = 10)
    print 'Result: %s' % r

#关闭
server.shutdown()


