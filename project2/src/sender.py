# ----- sender.py ------

#!/usr/bin/env python
from socket import *
import sys
import time 

numBytes = 0
message = ''
buf =1024 
s = socket(AF_INET,SOCK_DGRAM)
host =sys.argv[1]
port = int(sys.argv[2])
addr = (host,port)
data = ''
sequence = 0

def packets(data):
  content = bytearray(data.encode())
  packets = [content[i:i+buf-1] for i in range(0,len(content),buf)]
  return packets

#getting the data
for line in sys.stdin:
  data = data + line
 
mypackets = packets(data)

#wrap packets in header
for packet in mypackets:
  if sequence == 10:
    sequence = 0
  seqnum = bytearray(str(sequence).encode())
  packet += seqnum
  sequence += 1

i = 0
#make timer 
t_start = time.time()

while (i<len(mypackets)):
    #must implement try except 
  s.settimeout(2)
  try:
    if(s.sendto(mypackets[i],addr)):
      print("sending ...")
      #data = f.read(buf)
      #receive ACK, wait if not
      #try to receive message
      message,addr = s.recvfrom(buf)
      message = message.decode()
      print('i=' + str(i))
      print(message)
      numBytes += len(mypackets[i])
      i = i+1
          
  except Exception as stimeout:
      if timeout occurs, retransmit the packet 
      if(len(message)==0):
        j = 0
      else:
        seqnum = message[0]
       j = int(seqnum) +1
      print('j= ' + str(j))
      print("resending ...")
      #s.sendto(mypackets[j],addr)
      #message,addr = s.recvfrom(buf)
      #message = message.decode()
      i = j+1
  
s.close()

t_end = time.time()
kb = numBytes/1024
totalTime = t_end - t_start
print('Sent {} bytes in {}: {} kB/s'.format(numBytes, totalTime, (kb/totalTime)))
