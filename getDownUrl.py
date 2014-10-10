# -*- coding: utf-8 -*-
import re
import os
import urllib.request
#import httplib2
#import str
import base64
import pycurl
import io
import time

def createUrl(src):
    newsrc = src.replace('://',':##')
    dest = base64.b64encode(newsrc.encode())
    src = str(dest).replace('+','-')
    dest = src.replace('/','_')
    return 'http://api.flvxz.com/url/'+dest[2:-1]

def downUrlCurl(url):
	buf = io.StringIO()
	c = pycurl.Curl()
	c.setopt(c.URL, url)
	#c.setopt(c.COOKIEFILE, downUrl)
	#c.setopt(c.WRITEFUNCTION, buf.write)
	#c.setopt(c.CONNECTTIMEOUT, 5)
	#c.setopt(c.TIMEOUT, 60)
	#c.setopt(pycurl.USERAGENT, "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)")
	c.perform()
	page = buf.getvalue()
	buf.close()
	return page

def downUrlHttp(url):
	page = urllib.request.urlopen(url).read()
	return page

def downLibUrl(url):
	conn = HTTPConnection(url)
	conn.request('GET', '/', '', {'user-agent':'test'})
	res = conn.getresponse()
	conn.close()
	page = res.read()
	return page
	
def parser(src,pattern):
	src = src.decode('UTF-8')
	rebuf = re.findall(pattern,src)
	return rebuf

def deal():
    if os.path.exists('page.txt'):
        print('output file is exists\n')
        return 0

    if os.path.exists('r.txt') == False:
        print('r file is not exists\n')
        return 0

    if os.path.exists('w.txt') == False:
        print('w file is not exists\n')
        return 0

    regexlen = os.path.getsize('r.txt')
    fp = open("r.txt",'r')
    regexbuf = fp.read(regexlen)
    fp.close()
    regexlen = os.path.getsize('w.txt')
    fp = open("w.txt",'r')
    order = fp.read(regexlen)
    orderlist = order.split(',')
    fp.close()
    sleepsec = 20
    regexlen = os.path.getsize('s.txt')
    fp = open("s.txt",'r')
    sleepsec = int(fp.read(regexlen))
    fp.close()
    print('sleep sec:%d' % (sleepsec))
    print('write order:%s' % (order))
    pattern = re.compile(regexbuf)

    fp = open('url.txt','r')
    fpw = open('page.txt','w')
    count = 0

    while 1:
        url = fp.readline()
        if url=='':
            break
        if count > 0:
            time.sleep(sleepsec)
        newUrl = createUrl(url)
        #page = downUrlCurl(newUrl)
        print('down[%d]:%s'%(count,newUrl))
        page = downUrlHttp(newUrl)
        if page != '':
            rebuf = parser(page,pattern)
            print(len(rebuf))
            for i in range(0,len(rebuf)):
                    for j in orderlist:
                            if j.isdigit() == True:
                                    fpw.write(rebuf[i][int(j)])
                                    #fpw.write('\t')
                            else:
                                    fpw.write(j)
                    print (rebuf[i])
                    fpw.write('\n')
        count=count+1
    fpw.close()
    fp.close()
	
	
if __name__ == '__main__':
	deal()
	input('press any keys to quit.')
	
	
 
