'''
Created on 2016-6-6

@author: kjh
'''
import unittest
from test.my_dic import Dict

class Test(unittest.TestCase):


    def testName(self):
        pass
    
    def test_init(self):
        d = Dict(a= 1, b = 'test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, Dict))
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()