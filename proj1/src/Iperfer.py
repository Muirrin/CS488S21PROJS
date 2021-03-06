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
    
    
    if len(sys.argv) != 3:
            print('Error: missing or additional arguments')
    if int(sys.argv[1]) <= 1024 or int(sys.argv[1]) >= 65535:
            print('Error: port number must be in the range 1024 to 65535')
            
    def client(self, server_hostname,server_port,t):
            self.server_hostname = server_hostname
            self.server_port = server_port
            self.t = t
    # Create client socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP socket
# Ask for connection to server
    clientSocket.connect((server_hostname,server_port))
    t_end = time.time() + (60*t)
    while time.time() < t_end:
        clientSocket.send(data)
        clientSocket.recv(1000)
        data = data + 1000

    clientSocket.close()
    kb = numbytes/1000
    mb = (kb/1000) * 8
    rate = mb/t

    print('sent= {} KB rate={} Mbps'.format(numbytes,rate))
    #def __init__(self,name, port, time):
        #self.server_hostname = name
        #self.server_port = port
        #self.time = time



