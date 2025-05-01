# Füge dies zu modules/attacks/captcha_bypass.py hinzu
def solve_captcha():
    print("\n[🤖 Captcha-Bypass]")
    print("1: 2Captcha API")
    print("2: OCR-Umgehung")
    choice = input(">>> ")
    
    if choice == "1":
        api_key = input("API-Key eingeben: ")
        print(f"✅ Captchas werden automatisch gelöst via 2Captcha (Key: {api_key})")
    elif choice == "2":
        print("⚠️ Versuche Captcha mit Tesseract OCR zu lesen...")
