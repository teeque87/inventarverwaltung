import os
from services.item_services import ItemServices
from services.item_services import ItemServices

item_services = ItemServices()

def clear_console():
    # Leert die Konsole je nach Betriebssystem
    os.system('cls' if os.name == 'nt' else 'clear')

def artikel_anlegen(item_services: ItemServices):
    clear_console()
    try:
        product_id = int(input("Produkt-ID eingeben: "))
        name = input("Name des Artikels: ")
        amount = int(input("Anzahl: "))
        cat_id = int(input("Kategorie-ID: "))
        item_services.add_new_item(product_id, name, amount, cat_id)
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie die Daten erneut ein.")
    input("Drücken Sie Enter, um zum Menü zurückzukehren.")

def artikel_bearbeiten(item_services: ItemServices):
    clear_console()
    try:
        product_id = int(input("Produkt-ID des zu bearbeitenden Artikels: "))
        item_services.fetch_one_item(product_id)
        name = input("Neuer Name des Artikels: ")
        amount = int(input("Neue Anzahl: "))
        cat_id = int(input("Neue Kategorie-ID: "))
        item_services.add_new_item(product_id, name, amount, cat_id)
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie die Daten erneut ein.")
    input("Drücken Sie Enter, um zum Menü zurückzukehren.")

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
                artikel_anlegen(item_services)
            elif auswahl == 2:
                artikel_bearbeiten(item_services)
            elif auswahl == 3:
               """artikel_loeschen()"""
            elif auswahl == 4:
                clear_console()  # Konsole leeren, bevor zum Hauptmenü gewechselt wird
                print("Zurück zum Hauptmenü...")
                break
            else:
                print("Ungültige Auswahl! Bitte wählen Sie eine Option zwischen 1 und 4.")
        except ValueError:
            print("Fehler: Bitte geben Sie eine gültige Zahl ein.")