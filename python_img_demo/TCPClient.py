from socket import *
import sys


serverName = '10.3.22.177'
serverPort = 50007
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('Input lowercase sentence:')
print(sentence)
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ',modifiedSentence.decode())
sys.stdin.readline()
clientSocket.close()
