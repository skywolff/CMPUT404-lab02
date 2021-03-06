#!/bin/python3

import socket

HOST = 'www.google.com'
PORT = 8000
request = 'GET / HTTP/1.1\r\nHost: {}\r\n\r\n'.format(HOST)


def main():
    print(request)
    s = None
    for res in socket.getaddrinfo(
        HOST, PORT, family=socket.AF_INET, type=socket.SOCK_STREAM):
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
    with s:
        s.sendall(request.encode())
        s.settimeout(1.0)
        data = b""
        while True:
            try:
                part = s.recv(4096)
                data += part
            except socket.timeout:
                break
        print(data.decode('iso-8859-1'))


if __name__ == "__main__":
    main()
