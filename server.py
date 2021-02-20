# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 12:36:33 2021

@author: Sara Abbas
"""

import socket
import datetime

server = '127.0.0.1'
port = 80
receive_buffer_size = 4096

# server socket
# create UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind socket
serverSocket.bind((server, port))

while True:
# receive request - display date and time
      (serverReceive, (server, port)) = serverSocket.recvfrom(receive_buffer_size)
      print ("received request: ", serverReceive)
      now = datetime.datetime.now()
      print ("received on: ", now.strftime("%Y-%m-%d %H:%M:%S"))

# send echo request
      serverSocket.sendto(serverReceive, (server, port))

