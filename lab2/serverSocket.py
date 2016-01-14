#!/usr/bin/env python

import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(("0.0.0.0", 12345))
