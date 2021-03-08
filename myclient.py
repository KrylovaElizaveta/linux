#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
host = input('Write hostname:')
socnum = input('Write socket:')
if not host:
    host = 'localhost'
if not socnum:
    socnum = 1025
print('Connecting to server')
sock.connect((host, int(socnum)))
print('Connection complete')
print('My address', sock.getsockname())
data = sock.recv(1024)
if 'what is your name?' in data.decode():
    name = input("Hello, what's your name?\n")
    sock.send(name.encode())
else:
    print(data.decode())
s = input('Write message to server\n')
print('Sending data to server')
while s != "exit":
    sock.send(s.encode())
    print('Receiving data from server')
    data = sock.recv(1024)
    print('Answer: ', data.decode())
    s = input()
sock.send('exit'.encode())

print('End connection with server')
sock.close()



