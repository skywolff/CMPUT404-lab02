#!/bin/python3

import socket
import time



def mainInClass():
    HOST = ""
    PORT = 8001
    BUF_SIZE = 1024
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        while True:
            conn, clientAddr = s.accept()
            print("Connected by", addr)

            full_data = b""
            while True:
                data = conn.recv(BUF_SIZE)
                if not data: break
                full_data += data
            time.sleep(0.5)
            conn.sendall(full_data) 


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
    main()
