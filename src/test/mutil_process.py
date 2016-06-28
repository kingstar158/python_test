#_*_coding=utf-8_*_
'''
Created on 2016-6-13

@author: kjh
'''
import os
from multiprocessing import Process

print 'Process (%s) start' % os.getpid()

# 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'

