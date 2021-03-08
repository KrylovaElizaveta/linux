#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, errno
import json

try:
    open('clients.json', 'r')
except FileNotFoundError as e:
    with open('clients.json', 'w') as cl:
        cldict = dict()
        json.dump(cldict, cl) 

with open('log.txt', 'a') as log:
    log.write('Server starts working\n')
    sock = socket.socket()
    for i in range(1025, 65536):
        try:
            sock.bind(('', i))
            break
        except socket.error as e:
            if e.errno != errno.EADDRINUSE:
                log.write(e)
    log.write('Server\'s socket is '+str(sock.getsockname()[1])+'\n')
    print('Server\'s socket is '+str(sock.getsockname()[1]))
    while True:
        log.write('Server lisening the socket\n')
        sock.listen(1)
        conn, addr = sock.accept()

        log.write('Connected:'+ str(addr)+ '\n')
        log.write('Server say hello\n')
        with open('clients.json', 'r') as cl:
            cldict = json.load(cl)
            if cldict.get(str(addr[1])) != '' and cldict.get(str(addr[1])) != None:
                hello = "Hello, "+str(cldict.get(str(addr[1])))
                conn.send(hello.encode())
            else:
                conn.send("Hello, what is your name?".encode())
                name = conn.recv(1024)
                cldict[str(addr[1])]=name.decode()
        log.write('Server write to json file\n')
        with open('clients.json', 'w') as cl:
            json.dump(cldict, cl)
        log.write('Server receiving data from client\n')
        while True:
            data = conn.recv(1024)
            if data == 'exit'.encode():
                break
            if data:
                log.write('Server sending data to client\n')
                conn.send(data.upper())

        log.write('Server stops connection with'+  str(addr)+ '\n')    
        conn.close()


    log.write('Server stops working\n')

