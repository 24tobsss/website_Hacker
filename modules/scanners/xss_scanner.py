def scan(target_url):
    print(f"\n🔎 Scanne {target_url} auf XSS...")
    payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert(1)>"
    ]
    
    for payload in payloads:
        try:
            response = requests.get(target_url + payload)
            if payload in response.text:
                print(f"✅ XSS möglich mit: {payload}")
        except Exception as e:
            print(f"⚠️ Fehler: {e}")
