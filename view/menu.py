import os
from services.item_services import ItemServices

class Menu():
    def __init__(self):
        self.item_services = ItemServices()
        self.menue_auswahl()

    def clear_console(self):
        # Konsole je nach Betriebssystem leeren
        os.system('cls' if os.name == 'nt' else 'clear')

    def artikel_suchen(self):
        self.clear_console()
        print("\n********** Artikel suchen **********")
        print("1. Nach Artikel-ID suchen")
        print("2. Nach Produktnamen suchen")
        
        try:
            auswahl = int(input("\nBitte wählen Sie eine Option (1-2): "))
            
            if auswahl == 1:
                search_term = input("\nBitte geben Sie die Artikel-ID ein: ")
                try:
                    search_term = int(search_term)  # Konvertiere in Integer, da es eine ID ist
                except ValueError:
                    print("Ungültige Artikel-ID. Bitte eine Zahl eingeben.")
                    return  # Beendet die Methode, wenn die Eingabe ungültig ist

                results = self.item_services.search_items(str(search_term))  # Suche nach Artikel-ID

            elif auswahl == 2:
                search_term = input("\nBitte geben Sie den Produktnamen ein: ")
                results = self.item_services.search_items(search_term)  # Suche nach Produktname

            else:
                print("Ungültige Auswahl. Bitte wählen Sie entweder 1 oder 2.")
                return  # Beendet die Methode, wenn die Auswahl ungültig ist

            # Überprüfung, ob Ergebnisse gefunden wurden
            if results:
                print("\nGefundene Artikel:")
                for item in results:
                    print(f"ID: {item.product_id}, Name: {item.name}")
            else:
                print("Keine Artikel gefunden.")
            
        except ValueError:
            print("Fehler: Bitte geben Sie eine gültige Zahl ein.")
        
        input("\nDrücken Sie Enter, um zum Menü zurückzukehren.")

        # Artikel Menu
        def artikel_anlegen_bearbeiten(self):
            self.artikel_menue()

        def artikelgruppe_anlegen_bearbeiten(self):
            self.artikelgr_menue()

    # Artikel Menu
    def artikel_menue(self):
        while True:
            self.clear_console()
            print("\n********** Artikel anlegen / bearbeiten **********")
            print("1. Artikel anlegen")
            print("2. Artikel bearbeiten")
            print("3. Artikel löschen")
            print("4. Zurück zum Hauptmenü")
            print("**************************************************")
            
            try:
                auswahl = int(input("Bitte wählen Sie eine Option (1-4): "))
                
                if auswahl == 1:
                    self.clear_console()
                    print("\n******** Neuen Artikel anlegen ********\n")
                    try:
                        product_id = int(input("Produkt-ID eingeben: "))
                        name = input("Name des Artikels: ")
                        amount = int(input("Anzahl: "))
                        cat_id = int(input("Kategorie-ID: "))
                        self.item_services.add_new_entry(product_id, name, amount, cat_id)
                        input("\nDrücken Sie Enter, um zum Menü zurückzukehren.")
                    except ValueError:
                        print("Ungültige Eingabe. Bitte geben Sie die Daten erneut ein.")
                elif auswahl == 2:
                    self.clear_console()
                    print("\n******** Artikel bearbeiten ********")
                    try:
                        items = self.item_services.get_all_items()
                        for item in items:
                            print(item)
                        product_id = int(input("\nProdukt-ID eingeben: "))
                        name = input("Name des Artikels: ")
                        amount = int(input("Anzahl: "))
                        cat_id = int(input("Kategorie-ID: "))
                        self.item_services.add_new_entry(product_id, name, amount, cat_id)
                        input("\nDrücken Sie Enter, um zum Menü zurückzukehren.")
                    except ValueError:
                        print("Ungültige Eingabe. Bitte geben Sie die Daten erneut ein.")
                elif auswahl == 3:
                    self.clear_console()
                    print("\n******** Artikel löschen ********")
                    try:
                        items = self.item_services.get_all_items()
                        for item in items:
                            print(item)
                        product_id = int(input("\nProdukt-ID eingeben: "))
                        self.item_services.delete_entry(product_id)
                        input("\nDrücken Sie Enter, um zum Menü zurückzukehren.")
                    except ValueError:
                        print("Ungültige Eingabe. Bitte geben Sie die Daten erneut ein.")
                elif auswahl == 4:
                    self.clear_console()
                    print("Zurück zum Hauptmenü...")
                    break
                else:
                    print("Ungültige Auswahl! Bitte wählen Sie eine Option zwischen 1 und 4.")
            except ValueError:
                print("Fehler: Bitte geben Sie eine gültige Zahl ein.")

    # Artikelgruppen Menu
    def artikelgr_menue(self):
        while True:
            self.clear_console()
            print("\n********** Artikelgruppe anlegen / bearbeiten **********")
            print("1. Artikelgruppe anlegen")
            print("2. Artikelgruppe bearbeiten")
            print("3. Artikelgruppe löschen")
            print("4. Zurück zum Hauptmenü")
            print("********************************************************")
            
            try:
                auswahl = int(input("Bitte wählen Sie eine Option (1-4): "))
                
                if auswahl == 1:
                    self.artikelgr_anlegen()
                elif auswahl == 2:
                    self.artikelgr_bearbeiten()
                elif auswahl == 3:
                    self.artikelgr_loeschen()
                elif auswahl == 4:
                    self.clear_console()
                    print("Zurück zum Hauptmenü...")
                    break
                else:
                    print("Ungültige Auswahl! Bitte wählen Sie eine Option zwischen 1 und 4.")
            except ValueError:
                print("Fehler: Bitte geben Sie eine gültige Zahl ein.")

    def artikelgr_anlegen(self):
        self.clear_console()
        print("*** Artikelgruppe anlegen ***")
        try:
            categories = self.item_services.get_all_categories()
            for cat in categories:
                print(f"ID: {cat[0]:10} | Name: {cat[1]}")
            name = input("\nName der anzulegenden Kategorie: ")
            self.item_services.new_category(name)
            input("\nDrücken Sie Enter, um zum Menü zurückzukehren.")
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie die Daten erneut ein.")

    def artikelgr_bearbeiten(self):
        self.clear_console()
        print("*** Artikelgruppe bearbeiten ***")
        try:
            categories = self.item_services.get_all_categories()
            for cat in categories:
                print(f"ID: {cat[0]:10} | Name: {cat[1]}")
            cat_id = int(input("\nID der zu bearbeitenden Kategorie: "))
            name = input("Neuer Name der Kategorie: ")
            self.item_services.edit_category(cat_id, name)
            input("\nDrücken Sie Enter, um zum Menü zurückzukehren.")
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie die Daten erneut ein.")

    def artikelgr_loeschen(self):
        self.clear_console()
        print("*** Artikelgruppe löschen ***")
        try:
            categories = self.item_services.get_all_categories()
            for cat in categories:
                print(f"ID: {cat[0]:10} | Name: {cat[1]}")
            cat_id = int(input("\nID der zu löschenden Kategorie: "))
            self.item_services.delete_category(cat_id)
            input("\nDrücken Sie Enter, um zum Menü zurückzukehren.")
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie die Daten erneut ein.")

    def wareneingang(self):
        print("\n[Wareneingang ausgewählt]\n")
        input("Drücken Sie Enter, um zum Menü zurückzukehren.")

    def warenausgang(self):
        print("\n[Warenausgang ausgewählt]\n")
        input("Drücken Sie Enter, um zum Menü zurückzukehren.")

    def inventarliste_ausgeben(self):
        self.clear_console()
        print("********** Aktuell im Bestand **********")
        items = self.item_services.get_all_items()
        for item in items:
            print(item)
        input("\nDrücken Sie Enter, um zum Menü zurückzukehren.")

    def programm_beenden(self):
        print("\n[Programm wird beendet. Auf Wiedersehen!]\n")
        exit()

    def menue_anzeigen(self):
        print("\n********** Inventarverwaltung Hauptmenu **********")
        print("1. Artikel anlegen / bearbeiten")
        print("2. Artikelgruppe anlegen / bearbeiten")
        print("3. Wareneingang")
        print("4. Warenausgang")
        print("5. Inventarliste ausgeben")
        print("6. Artikel suchen")  # Option für die Suche hinzufügen
        print("7. Programm beenden")
        print("**************************************************")

    def menue_auswahl(self):
        while True:
            self.clear_console()  # Konsole leeren bevor das Hauptmenü angezeigt wird
            self.menue_anzeigen()
            try:
                auswahl = int(input("Bitte wählen Sie eine Option (1-7): "))
                
                if auswahl == 1:
                    self.artikel_anlegen_bearbeiten()
                elif auswahl == 2:
                    self.artikelgruppe_anlegen_bearbeiten()
                elif auswahl == 3:
                    self.wareneingang()
                elif auswahl == 4:
                    self.warenausgang()
                elif auswahl == 5:
                    self.inventarliste_ausgeben()
                elif auswahl == 6:
                    self.artikel_suchen()  # Aufruf der Suchfunktion
                elif auswahl == 7:
                    self.programm_beenden()
                else:
                    print("Ungültige Auswahl! Bitte wählen Sie eine Option zwischen 1 und 7.")
            except ValueError:
                print("Fehler: Bitte geben Sie eine gültige Zahl ein.")