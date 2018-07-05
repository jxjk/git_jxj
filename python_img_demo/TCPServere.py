import socket
import socketserver
import time
import threading


serverPort = 50007
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive.')
while 1 :
    connectionSocket,addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    # connectionSocket.send(capitalizedSentence)
    connectionSocket.send(bytes(time.ctime() + "\n",'utf-8') + capitalizedSentence)
    connectionSocket.close()
