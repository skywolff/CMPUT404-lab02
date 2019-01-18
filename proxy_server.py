#!/bin/python3
import socket
import time

def mainInClass():
    google_addr = None
    HOST = ""
    PORT = 8001
    BUF_SIZE = 1024

    addrInfo = socket.getaddrinfo(("www.google.com", PORT))
    for addr in addrInfo:
        (family, sockType, proto, canonname, sockaddr) = addr
        if family == socket.AF_INET and sockType == socket.SOCK_STREAM:
            google_addr = addr
            
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        while True:
            conn, clientAddr = s.accept()
            print("Connected by", addr)
            with socket.socket(family, sockType) as proxy_end:
                proxy_end.connect(sockaddr)
                send_full_data = b""
                while True:
                    data = conn.recv(BUF_SIZE)
                    if not data: break
                    full_data += data
                proxy_end.sendall(send_full_data)
                proxy_end.shutdown(socket.SHUT_WR)
                while True:
                    data = proxy_end.recv(BUF_SIZE)
                    print(data)
            time.sleep(0.5)
            conn.close()


def main():
    HOST = "127.0.0.1"
    PORT = 8000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        dataS, clientAddr = s.accept()
        with dataS:
            print("got connection from: ", clientAddr)
            while True:
                data = dataS.recv(1024)
                # if not data:
                    # break
                dataS.sendall(data)


if __name__ == "__main__":
    mainInClass()
