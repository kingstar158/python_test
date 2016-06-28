#_*_coding=utf-8_*_
'''
Created on 2016-6-3

@author: kjh
'''
import os
from dircache import listdir
    
class Search(object):
    
    def run(self):
        input_path = raw_input('Please input search path:')
        if input_path is None:
            return
        self.search(input_path)
        

    def search(self, path):
        if path is None:
            return
        s = os.path.abspath(path)
        if os.path.isdir(s):
            print s
            for i in os.listdir(s):
                self.search(os.path.join(s,i))
        elif os.path.isfile(s):
            print s     
        else:
            print '!!!'

