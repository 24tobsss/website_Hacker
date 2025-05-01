from main import colors
import os

def show():
    while True:
        os.system('clear')
        print(f"{colors.RED}")
        print("    ██████╗  █████╗ ███████╗██╗  ██╗")
        print("    ██╔══██╗██╔══██╗██╔════╝██║  ██║")
        print("    ██████╔╝███████║███████╗███████║")
        print("    ██╔══██╗██╔══██║╚════██║██╔══██║")
        print("    ██║  ██║██║  ██║███████║██║  ██║")
        print("    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")
        print(colors.END)
        
        print(f"{colors.BOLD}    [1] HTTP Flood")
        print("    [2] Slowloris")
        print("    [0] Zurück")
        choice = input(f"\n{colors.WHITE}    ► Auswahl: {colors.END}")
        
        if choice == "0":
            break
        else:
            print(f"\n{colors.YELLOW}⚠ Diese Funktion muss noch implementiert werden!{colors.END}")
            time.sleep(1)
