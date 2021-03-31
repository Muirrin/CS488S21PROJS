# ----- sender.py ------

#!/usr/bin/env python
from socket import *
import sys
import time 

numBytes = 0
buf =1024 
s = socket(AF_INET,SOCK_DGRAM)
host =sys.argv[1]
port = int(sys.argv[2])
addr = (host,port)
data = ''


def packets(data):
  content = bytearray(data.encode())
  packets = [content[i:i+buf] for i in range(0,len(content),buf)]
  return packets

#getting the data
for line in sys.stdin:
  data = data + sys.stdin.read(buf)
 
mypackets = packets(data)
i = 0
#make timer 
t_start = time.time()

while (i<len(mypackets)):
    if(s.sendto(mypackets[i],addr)):
        print("sending ...")
        #data = f.read(buf)
        numBytes += buf
        i = i+1

s.close()

t_end = time.time()
kb = numBytes/1024
totalTime = t_end - t_start
print('Sent {} bytes in {}: {} kB/s'.format(numBytes, totalTime, (kb/totalTime)))