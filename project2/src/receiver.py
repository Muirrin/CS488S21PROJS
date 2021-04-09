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
seqnum = 0

addr = ('',port)
buf=1024
t_start = time.time()
#f = open("received.txt",'wb')
message = ''
#receive
data,addr = s.recvfrom(buf)

#verify seqnum
#seqnum is the receivers value to test sequence
try:
    while(1):
        data = data.decode() #take the sequence number from the data
        sequence = data[len(data)-1]
        data = data[0:len(data)]
        sys.stdout.write(data)
        #if sequence and seqnum match -> send ack
        if sequence == str(seqnum):
          message = str(sequence) + 'ACK'
          message = bytearray(message.encode())
          s.sendto(message, addr)
          seqnum += 1
          if seqnum ==10:
            seqnum = 0
  
        s.settimeout(2)
        data,addr = s.recvfrom(buf)
except timeout:
    s.close()
    #print("File Downloaded")
