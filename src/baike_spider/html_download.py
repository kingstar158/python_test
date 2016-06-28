#_*_coding=utf-8_*_
'''
Created on 2016-6-2

@author: kjh
'''
import urllib2


class HtmlDownloader(object):
    
    
    def download(self, url):
        if url is None:
            return None
        
        response = urllib2.urlopen(url)
        
        
        result =  response.getcode()
        if result != 200:
            return None

        return response.read()
    
    



