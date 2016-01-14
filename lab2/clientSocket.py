#!/usr/bin/env/ python
# copyright (c) Ben Hunter

import socket

#AF_INET = want a socket on the internet (IP)
#Want a socket that allows us to talk to a stream (TCP)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(("www.google.com",80))
request = "GET / HTTP/1.0\n\n"
#request = "GET / HTTP/1.0\r\n\r\n"

clientSocket.sendall(request)

response = bytearray()
done = False

# if we are psychic and know exactly how much data we are getting
# from google, we could just put that in. But we don't
while not done:
    part = clientSocket.recv(1024)      # usually 1024 or 2048
    if part:
        response.extend(part)
    else:
        break

print response

