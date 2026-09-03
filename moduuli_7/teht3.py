airports = {
    "EFHK": "Helsinki Airport",
    "EFET": "Enontekiö Airport",
    "EFHA": "Halli Airport",
    "EFIV": "Ivalo Airport",
    "EFJO": "Joensuu Airport",
    "EFJY": "Jyväskylä Airport",
    "EFKT": "Kittilä Airport",
    "EFKK": "Kokkola-Pietarsaari Airport",
    "EFLP": "Lappeenranta Airport",
    "EFMA": "Mariehamn Airport",
    "EFOU": "Oulu Airport",
    "EFPO": "Pori Airport",
    "EFRO": "Rovaniemi Airport",
    "EFSA": "Savonlinna Airport",
    "EFTP": "Tampere-Pirkkala Airport",
    "EFTU": "Turku Airport",
    "EFUT": "Utti Airport",
    "EFVA": "Vaasa Airport",
}



while True:
    ans = input("If you want to enter new 'airport': enter 'new'.\nIf you want to search for existing 'airport': enter 'search'.\nIf you want to exit: enter 'exit'.")

    if ans == "exit":
        print("exiting...")
        break

    elif ans == "new":
        icao_code, name = input("\nEnter airports ICAO-code: "), input("\nEnter airports name: ")
        airports[icao_code] = name

        if airports[icao_code]:
            print(f"Airport with ICAO-code {icao_code} added. Name: {airports[icao_code]}")

    elif ans == "search":
        icao_code = input("\nEnter airports ICAO-code: ")
        print(f"\nAirport code: '{icao_code}' name: {airports[icao_code]}\n")
