import sys
import socket 
import os

TCP_IP = "127.0.0.1"
TCP_PORT = 5005
FNAME = 'Img.jpg'

print "TCP target IP:", TCP_IP
print "TCP target port:", TCP_PORT
print "Image Name:", FNAME


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((TCP_IP,TCP_PORT))
sock.listen(10)

while True:
    data,addr = sock.accept()
    Path = r'IMG/' 
    if not os.path.exists(Path):
        os.makedirs(Path)

    fileUpload = open(Path+FNAME,"wb")
    sData = data.recv(1024)
    while sData:
        fileUpload.write(sData)
        sData = data.recv(1024)
    print "Completed"
sock.close()
