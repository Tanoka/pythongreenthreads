#!/usr/bin/env python3 
""" 
This is a simple web "crawler" that fetches a bunch of urls using a pool to 
control the number of outbound connections. It has as many simultaneously open 
connections as coroutines in the pool. 
 
The prints in the body of the fetch function are there to demonstrate that the 
requests are truly made in parallel. 

INSTALL:
RUN apt -y install python3
RUN apt-get -y install python3-pip
RUN apt-get -y install python3-eventlet


OUTPUT:
opening https://www.google.com/intl/en_ALL/images/logo.gif
opening http://python.org/images/python-logo.gif
opening http://us.i1.yimg.com/us.yimg.com/i/ww/beta/y3.gif
done with http://us.i1.yimg.com/us.yimg.com/i/ww/beta/y3.gif
done with https://www.google.com/intl/en_ALL/images/logo.gif
got body from https://www.google.com/intl/en_ALL/images/logo.gif of length 8558
done with http://python.org/images/python-logo.gif
got body from http://python.org/images/python-logo.gif of length 2549
got body from http://us.i1.yimg.com/us.yimg.com/i/ww/beta/y3.gif of length 1874


""" 
import eventlet 
from eventlet.green.urllib import request 

import time 
urls = [ 
    "http://www.byhours.com",
    "https://www.google.com/intl/en_ALL/images/logo.gif", 
    "http://python.org/images/python-logo.gif", 
    "http://us.i1.yimg.com/us.yimg.com/i/ww/beta/y3.gif", 
] 
 
 
def fetch(url): 
    stt = time.time()
    print("opening", url) 
    body = request.urlopen(url).read() 
    print("done with", url) 
    print('-----> Time func:', time.time() - stt, 'sec')   
    return url, body 
 
 
#Pool of green threads, size=200
pool = eventlet.GreenPool(200) 

st = time.time()

#iterator.imap each iteration is executed in a separate green thread
# .imap(function name, params)
for url, body in pool.imap(fetch, urls): 
    print("got body from", url, "of length", len(body))

print('\nTime End:', time.time() - st, 'sec')   
