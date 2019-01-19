#!/bin/python3

import socket
import selectors

BUF_SIZE = 1024
sel = selectors.DefaultSelector()

def main():
    serverEndAddrInfo = \
        socket.getaddrinfo("www.google.com", 80, socket.AF_INET, socket.SOCK_STREAM)
    for addrInfo in serverEndAddrInfo:
        family, type, proto, canonname, sockaddr = addrInfo

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientEnd:
        clientEnd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        clientEnd.bind(("localhost", 8001))
        clientEnd.listen()
        while True:
            conn, clientAddr = clientEnd.accept()
            print("got connection from: ", clientAddr)

            with socket.socket(family, type) as serverEnd:
                serverEnd.connect(sockaddr)

                data = b""
                while True:
                    part = conn.recv(BUF_SIZE)
                    if not part: break
                    data += part

            serverEnd.sendall(data)
            serverEnd.shutdown(socket.SHUT_WR)

            while True:
                data = serverEnd.recv(BUFFER_SIZE)
                if not data: break
                conn.send(data)

        conn.close()


if __name__ == "__main__":
    main()
