#_*_coding=utf-8_*_
'''
Created on 2016-6-16

@author: kjh
'''
import threading

balance = 0
### lock 的使用
lock = threading.Lock()


def change_info(n):
    global balance
    lock.acquire()
    try:
        balance = balance + n
        balance = balance - n
    finally:
        lock.release()
         
    

def run_thread(n):
    for i in range(10000):
            change_info(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()

print balance