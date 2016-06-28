#_*_coding=utf-8_*_
'''
Created on 2016-6-3

@author: kjh
'''
from FileSystem import search


class FileSystem(object):
    def __init__(self):
        self.search = search.Search()
    
    def local_run(self):
        print '-------------功能菜单---------------'
        print '-   1. search                   -'
        print '---------------------------------'
        
        input_num = input('Please input number:')
        
        if input_num  == 1:
            self.search.run()



if __name__ == "__main__":
    obj = FileSystem()
    obj.local_run()
    