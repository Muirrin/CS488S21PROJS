import socket
import sys
import time

class iperfer:
    numbytes = 0
    data = 0
    kb = 0
    mb = 0
    #rate is just mbps
    rate = 0
    sentbytes = 0
    
    if len(sys.argv) != 4:
        print('Error: missing or additional arguments')
        sys.exit(1)
    hostname = str(sys.argv[1])
    port = int(sys.argv[2])
    mytime = int(sys.argv[3])
    if port <= 1024 or port >= 65535:
        print('Error: port number must be in the range 1024 to 65535') 
   #def client(self, server_hostname,server_port,t):
      #  self.server_hostname = server_hostname
       # self.server_port = server_port
        #self.t = t
    # Create client socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP socket
# Ask for connection to server
    clientSocket.connect((hostname,port))
   # t_end = time.time() + (mytime)
    t_start = time.time()
    t_end = t_start + mytime 
    elapsed = t_end - t_start
    while  elapsed >= 0:
#    while time.time() < t_end:
        clientSocket.send(bytes(data))
        data = data + 1000
        t_start = time.time()
        elapsed =  t_end - t_start

    clientSocket.close()
    print(data)
    kb = data/1000
    mb = (kb/1000) * 8
    rate = mb/mytime

    print('sent= {} KB rate={} Mbps'.format(kb,rate))
    #def __init__(self,name, port, time):
        #self.server_hostname = name
        #self.server_port = port
        #self.time = time



