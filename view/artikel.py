import os

def clear_console():
    # Leert die Konsole je nach Betriebssystem
    os.system('cls' if os.name == 'nt' else 'clear')

def artikel_menue():
    while True:
        clear_console()  # Konsole leeren, bevor das Artikelmenü angezeigt wird
        print("\n********** Artikel anlegen / bearbeiten **********")
        print("1. Artikel anlegen")
        print("2. Artikel bearbeiten")
        print("3. Artikel löschen")
        print("4. Zurück zum Hauptmenü")
        print("**************************************************")
        
        try:
            auswahl = int(input("Bitte wählen Sie eine Option (1-4): "))
            
            if auswahl == 1:
                artikel_anlegen()
            elif auswahl == 2:
                artikel_bearbeiten()
            elif auswahl == 3:
                artikel_loeschen()
            elif auswahl == 4:
                clear_console()  # Konsole leeren, bevor zum Hauptmenü gewechselt wird
                print("Zurück zum Hauptmenü...")
                break
            else:
                print("Ungültige Auswahl! Bitte wählen Sie eine Option zwischen 1 und 4.")
        except ValueError:
            print("Fehler: Bitte geben Sie eine gültige Zahl ein.")