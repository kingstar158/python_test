'''
Created on 2016-6-13

@author: kjh
'''
import json

class Student(object):
    
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        

def std2json(std):
    return {
            'name': std.name,
            'age': std.age,
            'score': std.score
            }

s = Student('Hell', 12, 98)
#print (json.dumps(s, default = std2json))
print(json.dumps(s, default=lambda obj: obj.__dict__))