from main import colors, show_logo, log_action
import os
import subprocess
import requests
import socket
import time
from concurrent.futures import ThreadPoolExecutor

# --- WPScan ---
def run_wpscan(target):
    show_logo()
    print(f"\n{colors.BLUE}🔎 Starting WPScan...{colors.END}")
    log_file = f"logs/wpscan_{target.replace('://', '_').replace('/', '_')}.txt"
    try:
        cmd = f"wpscan --url {target} --enumerate vp,vt --no-update -o {log_file}"
        subprocess.run(cmd, shell=True, check=True)
        print(f"{colors.GREEN}✅ Scan complete! Results in {log_file}{colors.END}")
        log_action(target, "WPSCAN", f"Results in {log_file}")
    except Exception as e:
        print(f"{colors.RED}✘ Error: {str(e)}{colors.END}")
    input(f"\n{colors.YELLOW}↵ Press Enter...{colors.END}")

# --- Nikto Scan ---
def run_nikto(target):
    show_logo()
    print(f"\n{colors.BLUE}🔎 Starting Nikto Scan...{colors.END}")
    log_file = f"logs/nikto_{target.replace('://', '_').replace('/', '_')}.xml"
    try:
        cmd = f"nikto -h {target} -output {log_file} -Format xml"
        subprocess.run(cmd, shell=True, check=True)
        print(f"{colors.GREEN}✅ Scan complete! Results in {log_file}{colors.END}")
        log_action(target, "NIKTO", f"Results in {log_file}")
    except Exception as e:
        print(f"{colors.RED}✘ Error: {str(e)}{colors.END}")
    input(f"\n{colors.YELLOW}↵ Press Enter...{colors.END}")

# --- Portscan ---
def port_scan(target):
    show_logo()
    print(f"\n{colors.BLUE}🔎 Starting Portscan...{colors.END}")
    ports = [21, 22, 80, 443, 3306, 8080]
    host = target.split("//")[-1].split("/")[0] if "//" in target else target
    
    def scan_port(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((host, port))
                return port, True
        except:
            return port, False
    
    open_ports = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(scan_port, ports)
        for port, is_open in results:
            if is_open:
                print(f"{colors.GREEN}✔ Port {port} open{colors.END}")
                open_ports.append(str(port))
            else:
                print(f"{colors.RED}✘ Port {port} closed{colors.END}")
    
    log_action(target, "PORTSCAN", f"Open ports: {', '.join(open_ports)}")
    input(f"\n{colors.YELLOW}↵ Press Enter...{colors.END}")

# --- Scanner Menu ---
def menu():
    while True:
        show_logo()
        print(f"{colors.BOLD}    [1] SQL Injection Scan")
        print("    [2] WPScan (WordPress)")
        print("    [3] Nikto Scan")
        print("    [4] Portscan")
        print("    [0] Back")
        
        choice = input(f"\n{colors.WHITE}    ► Scan choice: {colors.END}")
        
        if choice == "0":
            return
        elif choice in ["1", "2", "3", "4"]:
            target = input(f"{colors.WHITE}    ► Target URL/IP: {colors.END}")
            if choice == "1":
                import attacks
                attacks.sql_injection(target, scan_mode=True)
            elif choice == "2":
                run_wpscan(target)
            elif choice == "3":
                run_nikto(target)
            elif choice == "4":
                port_scan(target)
