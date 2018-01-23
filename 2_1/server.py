#!/usr/bin/env python

import socket

def fac(n):
   if n == 1:
       return n
   else:
       return n*fac(n-1)

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    print 'Connection address:', addr
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        result = fac(int(data))
        print "received data:", data
        print "Result:", result
        conn.send(str(result))  # echo
    conn.close()
