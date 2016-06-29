#_*_coding=utf-8_*_
'''
Created on 2016-6-2

@author: kjh
'''


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    
    def collect_data(self, data):
        if data is None:
            return
        
        self.datas.append(data)
        

    
    def output_html(self):
        # with open('output.html', 'w') as fout   可防止遗忘调用close方法
        fout = open('output.html', 'w')
        
        fout.write("<html>")
        fout.write("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />")
        fout.write("<body>")
        fout.write("<table>")
        
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td> %s </td>" % data['url'])
            fout.write("<td> %s </td>" % data['title'].encode('utf-8'))
            fout.write("<td> %s </td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
            
        fout.write("</html>")
        fout.write("</body>")
        fout.write("</table>")
        
        fout.close()
    
    
    



