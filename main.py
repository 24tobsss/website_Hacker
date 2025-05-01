#!/usr/bin/env python3
import os
import sys
import time
from getpass import getpass
from datetime import datetime

# --- Colors ---
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

# --- Logo ---
def show_logo():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""{colors.RED}
    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
    ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    {colors.END}""")

# --- Logging ---
def log_action(target, action, result):
    os.makedirs("logs", exist_ok=True)
    domain = target.replace("http://", "").replace("https://", "").split("/")[0]
    with open(f"logs/{domain}.log", "a") as f:
        f.write(f"[{datetime.now()}] {action.upper()}: {result}\n")

# --- Password Check ---
def check_password():
    show_logo()
    print(f"\n{colors.RED}")
    print("    █████████████████████████████████")
    print("    ████                         ████")
    print("    ████                         ████")
    print("    ████       🔒 LOCKED 🔒      ████")
    print("    ████                         ████")
    print("    ████                         ████")
    print("    █████████████████████████████████")
    print(colors.END)
    
    if getpass(f"{colors.WHITE}    ► Password: {colors.END}") == "hack5":
        print(f"\n{colors.GREEN}")
        print("    █████████████████████████████████")
        print("    ████                         ████")
        print("    ████                         ████")
        print("    ████       🟢 OPEN 🟢        ████")
        print("    ████                         ████")
        print("    ████                         ████")
        print("    █████████████████████████████████")
        print(colors.END)
        time.sleep(1)
        return True
    print(f"\n{colors.RED}✘ Wrong password!{colors.END}")
    time.sleep(1)
    return False

# --- Main Menu ---
def main():
    os.makedirs("logs", exist_ok=True)
    
    while True:
        show_logo()
        print(f"{colors.BOLD}    [1] Scanner Suite")
        print("    [2] Attack Mode (Password: hack5)")
        print("    [0] Exit")
        
        choice = input(f"\n{colors.WHITE}    ► Selection: {colors.END}")
        
        if choice == "1":
            import scanners
            scanners.menu()
        elif choice == "2":
            if check_password():
                import attacks
                attacks.menu()
        elif choice == "0":
            print(f"\n{colors.CYAN}🛑 Shutting down...{colors.END}")
            sys.exit(0)

if __name__ == "__main__":
    main()
