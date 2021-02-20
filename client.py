# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 12:36:39 2021

@author: Sara Abbas
"""

import socket
import time

server = '127.0.0.1'
port = 80
receive_buffer_size = 4096

# client socket
# create UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send and receive 5 consecutive echo requests 
i = 1
L = []
request = 'echo request'
requestByte = request.encode('ascii')
while i < 6:
    t1 = time.time() # start time
    clientSocket.sendto(requestByte, (server, port)) # send echo request
    (clientReceive, (server, port)) = clientSocket.recvfrom(receive_buffer_size) # receive echo request
    print ("received echo request: ", clientReceive)
    t2 = time.time()
    RTT = t2 - t1
    print ("round trip time for echo request nb ",i,": ", RTT) # display RTT for each request
    L.append(RTT)
    i = i+1
    

j = 0    
totalRTT = 0 
while j < 5:
    totalRTT = totalRTT + L[j]
    j = j+1  
print ("average RTT: ",totalRTT/5)

clientSocket.close()
