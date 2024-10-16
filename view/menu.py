import view.artikel  # importieren des Unterprogramms artikel.py
import view.artikelgr # importieren des Unterprogramms artikelgr.py
from services.item_services import ItemServices
import os

def clear_console():
    # Konsole je nach Betriebssystem
    os.system('cls' if os.name == 'nt' else 'clear')

def artikel_anlegen_bearbeiten():
    # Aufruf des Unterprogramms artikel.py
    artikel.artikel_menue()

def artikelgruppe_anlegen_bearbeiten():
    #aufrufen des Unterprogramms artikelgr.py
    artikelgr.artikelgr_menue()

def wareneingang():
    print("\n[Wareneingang ausgewählt]\n")
    input("Drücken Sie Enter, um zum Menü zurückzukehren.")

def warenausgang():
    print("\n[Warenausgang ausgewählt]\n")
    input("Drücken Sie Enter, um zum Menü zurückzukehren.")

def inventurliste_ausgeben():
    clear_console()
    ItemServices().fetch_all_items()
    input("Drücken Sie Enter, um zum Menü zurückzukehren.")

def programm_beenden():
    print("\n[Programm wird beendet. Auf Wiedersehen!]\n")
    exit()

def menue_anzeigen():
    print("\n********** Inventarverwaltung Hauptmenu **********")
    print("1. Artikel anlegen / bearbeiten")
    print("2. Artikelgruppe anlegen / bearbeiten")
    print("3. Wareneingang")
    print("4. Warenausgang")
    print("5. Inventurliste ausgeben")
    print("6. Programm beenden")
    print("**************************************************")

def menue_auswahl():
    while True:
        clear_console()  # Konsole leeren bevor das Hauptmenü angezeigen
        menue_anzeigen()
        try:
            auswahl = int(input("Bitte wählen Sie eine Option (1-6): "))
            
            if auswahl == 1:
                artikel_anlegen_bearbeiten()
            elif auswahl == 2:
                artikelgruppe_anlegen_bearbeiten()
            elif auswahl == 3:
                wareneingang()
            elif auswahl == 4:
                warenausgang()
            elif auswahl == 5:
                inventurliste_ausgeben()
            elif auswahl == 6:
                programm_beenden()
            else:
                print("Ungültige Auswahl! Bitte wählen Sie eine Option zwischen 1 und 6.")
        except ValueError:
            print("Fehler: Bitte geben Sie eine gültige Zahl ein.")

if __name__ == "__main__":
    menue_auswahl()