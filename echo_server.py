#!/bin/python3

import socket

HOST = "127.0.0.1"
PORT = 8000


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        dataS, clientAddr = s.accept()
        with dataS:
            print("got connection from: ", clientAddr)
            while True:
                data = dataS.recv(1024)
                print(data)
                dataS.sendall(data)


if __name__ == "__main__":
    main()
