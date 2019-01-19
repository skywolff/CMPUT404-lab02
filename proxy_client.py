#!/bin/python3

import socket

HOST = 'www.google.com'
PORT = 80
request = 'GET / HTTP/1.1\r\nHost: {}\r\n\r\n'.format(HOST)


def main():
    print(request)
    s = None
    for res in socket.getaddrinfo(
            "localhost", 8001, family=socket.AF_INET, type=socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
            s.connect(sa)
        except OSError:
            if s: s.close()
            continue
        break
    if s is None:
        print("failed to connect to server")
        return

    s.send(request.encode())
    s.shutdown(socket.SHUT_WR)

    data = b""
    while True:
        part = s.recv(4096)
        if not part: break
        data += part
    print(data.decode('iso-8859-1'))
    s.close()


if __name__ == "__main__":
    main()
