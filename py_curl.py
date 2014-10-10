
#import pycurl
#import cStringIO

#c=pycurl.Curl()
#buf=cStringIO.StringIO()

#c.setopt(c.URL, 'http://www.baidu.com')
#c.setopt(c.WTRTEFUNCTION, buf.write)
#c.perform()

#print buf.getvalue()

#buf.close()

import pycurl
import io
 
buf = io.StringIO()
 
crl = pycurl.Curl()
crl.setopt(crl.URL, 'http://hd.baofeng.com/play/163/play-763163.html')
crl.setopt(crl.COOKIEFILE, 'http://hd.baofeng.com/play/163/play-763163.html')
crl.setopt(crl.WRITEFUNCTION, buf.write)
crl.setopt(crl.CONNECTTIMEOUT, 5)
crl.setopt(crl.TIMEOUT, 8)
#c.setopt(c.PROXY, 'http://inthemiddle.com:8080')
#crl.perform()

print (buf.getvalue())
buf.close()


