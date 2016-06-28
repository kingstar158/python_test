#_*_coding=utf-8_*_
'''
Created on 2016-6-6

@author: kjh
'''

class Dict(dict):
    
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)
        
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dist' object has no attibute %s" %key)
    
    def __setattr__(self, key, value):
        self[key] = value
        

