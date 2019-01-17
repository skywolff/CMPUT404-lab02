#!/bin/python3

import socket

HOST = 'www.google.com'
PORT = 80
request = 'GET / HTTP/1.1\r\n\r\n'


def main():
    print(request)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bytearray(request, 'utf-8'))
        s.settimeout(0.1)
        while True:
            try:
                response = s.recv(4096)
                print(response.decode('iso-8859-1'))
                # print(response.decode('utf-8'))
            except socket.timeout:
                return


if __name__ == "__main__":
    main()
