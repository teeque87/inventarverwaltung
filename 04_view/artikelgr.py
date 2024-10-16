import os

def clear_console():
    # Leert die Konsole je nach Betriebssystem
    os.system('cls' if os.name == 'nt' else 'clear')

def artikelgr_menue():
    while True:
        clear_console()  # Konsole leeren, bevor das Artikelmenü angezeigt wird
        print("\n********** Artikelgruppe anlegen / bearbeiten **********")
        print("1. Artikelgruppe anlegen")
        print("2. Artikelgruppe bearbeiten")
        print("3. Artikelgruppe löschen")
        print("4. Zurück zum Hauptmenü")
        print("********************************************************")
        
        try:
            auswahl = int(input("Bitte wählen Sie eine Option (1-4): "))
            
            if auswahl == 1:
                artikelgr_anlegen()
            elif auswahl == 2:
                artikelgr_bearbeiten()
            elif auswahl == 3:
                artikelgr_loeschen()
            elif auswahl == 4:
                clear_console()  # Konsole leeren und zurück zum Hauptmenu
                print("Zurück zum Hauptmenü...")
                break
            else:
                print("Ungültige Auswahl! Bitte wählen Sie eine Option zwischen 1 und 4.")
        except ValueError:
            print("Fehler: Bitte geben Sie eine gültige Zahl ein.")