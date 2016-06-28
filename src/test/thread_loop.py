'''
Created on 2016-6-16

@author: kjh
'''
import threading, multiprocessing

def loop():
    i = 10
    while(True):
        i = i ^ 1
        

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()