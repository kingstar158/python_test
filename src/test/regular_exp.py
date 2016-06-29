#_*_coding=utf-8_*_
'''
Created on 2016-6-29

@author: kjh
'''

import re

#re.match(r'^\d[3}\-\d{3,8}$', '010-12345')
#re.match(r'^\d{3}\-\d{3,8}$', '010 12345')

#Email地址验证表达式
#re_email = re.compile(r'(\<[\w\s]+\>\s*)?\s([a-zA-Z0-9\_]+)@([a-zA-Z0-9]+)\.(a-zA-Z[2,3])$')
re_email = re.compile(r'(\<[\w\s]+\>)?\s*([a-zA-Z0-9\_\.]+)@([a-zA-Z0-9]+).([a-zA-Z]{2,3})$')


#re_test = re.compile(r'(\<[\w\s]+\>\s*)?')
#print re_test.match('a').group(0)

#Email list
email_1 = 'someone@gmail.com'
email_2 = 'bill.gates@microsoft.com'
email_3 = '<Tom Paris> tom@voyager.org'
email_4 = '<Zhaoyn>zhaoyn@bbtree.com'
email_5 = '79152045@qq.com'
email_6 = 'zhao_79152045@163.com'


if re_email.match(email_1):
    print re_email.match(email_1).group(0)
else:
    print 'Fail!!'
print re_email.match(email_2).group(0);
print re_email.match(email_3).group(0);
print re_email.match(email_4).group(0);
print re_email.match(email_5).group(0);
print re_email.match(email_6).group(0);
