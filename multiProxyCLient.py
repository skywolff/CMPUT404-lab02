#!/bin/python3
import socket
from multiprocessing import pool

HOST = "localhost"
PORT = 8001
BUF_SIZE = 1024
request = 'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'

def main():
    addrInfo = socket.getaddrinfo(HOST, PORT)
    for addr in addrInfo:
        (family, sockType, proto, canonname, sockaddr) = addr
        if family == socket.AF_INET and sockType == socket.SOCK_STREAM:
            print(addr)
            get_request(addr)

def get_request(addr):
    (family, sockType, proto, canonname, sockaddr) = addr
    try: 
        s = socket.socket(family, sockType, proto)
        s.connect((HOST,PORT))
        s.sendall(request.encode())
        s.shutdown(socket.SHUT_WR)
        full_data = b""
        while True:
            data = s.recv(BUF_SIZE)
            if not data: break
            full_data += data
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        s.close()


def main2():
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
