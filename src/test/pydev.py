#_*_coding=utf-8_*_
'''
Created on 2016-5-26

@author: kjh
'''
import urllib2
import cookielib
print 'Hello world!'

url = "https://www.baidu.com/"
print '第一种方法'
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())


print '第二种方法'
request = urllib2.Request(url)
request.add_header("user-agent", "Mazilla/5.0")
reponse2 = urllib2.urlopen(request)
print reponse2.getcode()
print len(reponse2.read())


print '第三种方法'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print cj
print response3.read()
