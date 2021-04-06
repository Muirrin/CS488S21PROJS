# ----- receiver.py -----

#!/usr/bin/env python

from socket import *
import sys
import select
import time

#host="10.0.0.2"
host = ''
port = int(sys.argv[1])
s = socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))

addr = ('',port)
buf=1024
t_start = time.time()
#f = open("received.txt",'wb')

data,addr = s.recvfrom(buf)

try:
    while(1):
        data = data.decode()
        sys.stdout.write(data)
        s.settimeout(2)
        data,addr = s.recvfrom(buf)
except timeout:
    
    s.close()
    print("File Downloaded")
