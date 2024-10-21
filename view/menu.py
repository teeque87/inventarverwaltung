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
        search_term = input("Bitte geben Sie den Produktnamen oder die Produkt-ID ein: ")

        results = self.item_services.search_items(search_term)

        if results:
            print("\nGefundene Artikel:")
            for item in results:
                print(f"ID: {item[0]}, Name: {item[1]}, Anzahl: {item[2]}, Kategorie-ID: {item[3]}")
        else:
            print("Keine Artikel gefunden.")
        
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
            primport os
from services.item_services import ItemServices

class Menu():
    def __init__(self):
        self.item_services = ItemServices()
        self.menue_auswahl()

    def clear_console(self):
        # Konsole je nach Betriebssystem
        os.system('cls' if os.name == 'nt' else 'clear')

    # Untermenu Funktionen
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
        print("6. Programm beenden")
        print("**************************************************")

    def menue_auswahl(self):
        while True:
            self.clear_console()  # Konsole leeren bevor das Hauptmenü angezeigen
            self.menue_anzeigen()
            try:
                auswahl = int(input("Bitte wählen Sie eine Option (1-6): "))
                
                import os
from services.item_services import ItemServices

class Menu():
    def __init__(self):
        self.item_services = ItemServices()
        self.menue_auswahl()

    def clear_console(self):
        # Konsole je nach Betriebssystem
        os.system('cls' if os.name == 'nt' else 'clear')

    # Untermenu Funktionen
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
            print("Ungimport os
from services.item_services import ItemServices

class Menu():
    def __init__(self):
        self.item_services = ItemServices()
        self.menue_auswahl()

    def clear_console(self):import os
from services.item_services import ItemServices

class Menu():
    def __init__(self):
        self.item_services = ItemServices()
        self.menue_auswahl()

    def clear_console(self):
        # Konsole je nach Betriebssystem
        os.system('cls' if os.name == 'nt' else 'clear')

    # Untermenu Funktionen
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
                print(f"ID: {caimport os
from services.item_services import ItemServices

class Menu():
    def __init__(self):
        self.item_services = ItemServices()
        self.menue_auswahl()

    def clear_console(self):
        # Konsole je nach Betriebssystem
        os.system('cls' if os.name == 'nt' else 'clear')

    # Untermenu Funktionen
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
        self.clear_console()import os
from services.item_services import ItemServices

class Menu():
    def __init__(self):
        self.item_services = ItemServices()
        self.menue_auswahl()

    def clear_console(self):
        # Konsole je nach Betriebssystem
        os.system('cls' if os.name == 'nt' else 'clear')

    # Untermenu Funktionen
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
        print("6. Programm beenden")
        print("**************************************************")

    def menue_auswahl(self):
        while True:
            self.clear_console()  # Konsole leeren bevor das Hauptmenü angezeigen
            self.menue_anzeigen()
            try:
                auswahl = int(input("Bitte wählen Sie eine Option (1-6): "))
                
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
                    self.programm_beenden()
                else:
                    print("Ungültige Auswahl! Bitte wählen Sie eine Option zwischen 1 und 6.")
            except ValueError:
                print("Fehler: Bitte geben Sie eine gültige Zahl ein.")
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
        print("6. Programm beenden")
        print("**************************************************")

    def menue_auswahl(self):
        while True:
            self.clear_console()  # Konsole leeren bevor das Hauptmenü angezeigen
            self.menue_anzeigen()
            try:
                auswahl = int(input("Bitte wählen Sie eine Option (1-6): "))
                
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
                    self.programm_beenden()
                else:
                    print("Ungültige Auswahl! Bitte wählen Sie eine Option zwischen 1 und 6.")
            except ValueError:
                print("Fehler: Bitte geben Sie eine gültige Zahl ein.")t[0]:10} | Name: {cat[1]}")
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
        print("6. Programm beenden")
        print("**************************************************")

    def menue_auswahl(self):
        while True:
            self.clear_console()  # Konsole leeren bevor das Hauptmenü angezeigen
            self.menue_anzeigen()
            try:
                auswahl = int(input("Bitte wählen Sie eine Option (1-6): "))
                
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
                    self.programm_beenden()
                else:
                    print("Ungültige Auswahl! Bitte wählen Sie eine Option zwischen 1 und 6.")
            except ValueError:
                print("Fehler: Bitte geben Sie eine gültige Zahl ein.")
        # Konsole je nach Betriebssystem
        os.system('cls' if os.name == 'nt' else 'clear')

    # Untermenu Funktionen
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
        print("6. Programm beenden")
        print("**************************************************")

    def menue_auswahl(self):
        while True:
            self.clear_console()  # Konsole leeren bevor das Hauptmenü angezeigen
            self.menue_anzeigen()
            try:
                auswahl = int(input("Bitte wählen Sie eine Option (1-6): "))
                
                if auswahl == 1:
                    self.artikel_anlegen_bearbeiten()
                elif aimport os
from services.item_services import ItemServices

class Menu():
    def __init__(self):
        self.item_services = ItemServices()
        self.menue_auswahl()

    def clear_console(self):
        # Konsole je nach Betriebssystem
        os.system('cls' if os.name == 'nt' else 'clear')

    # Untermenu Funktionen
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
        print("6. Programm beenden")
        print("**************************************************")

    def menue_auswahl(self):
        while True:
            self.clear_console()  # Konsole leeren bevor das Hauptmenü angezeigen
            self.menue_anzeigen()
            try:
                auswahl = int(input("Bitte wählen Sie eine Option (1-6): "))
                
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
                    self.programm_beenden()
                else:
                    print("Ungültige Auswahl! Bitte wählen Sie eine Option zwischen 1 und 6.")
            except ValueError:
                print("Fehler: Bitte geben Sie eine gültige Zahl ein.")uswahl == 2:
                    self.artikelgruppe_anlegen_bearbeiten()
                elif auswahl == 3:
                    self.wareneingang()
                elif auswahl == 4:
                    self.warenausgang()
                elif auswahl == 5:
                    self.inventarliste_ausgeben()
                elif auswahl == 6:
                    self.programm_beenden()
                else:
                    print("Ungültige Auswahl! Bitte wählen Sie eine Option zwischen 1 und 6.")
            except ValueError:
                print("Fehler: Bitte geben Sie eine gültige Zahl ein.")ültige Eingabe. Bitte geben Sie die Daten erneut ein.")


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
        print("6. Programm beenden")
        print("**************************************************")

    def menue_auswahl(self):
        while True:
            self.clear_console()  # Konsole leeren bevor das Hauptmenü angezeigen
            self.menue_anzeigen()
            try:
                auswahl = int(input("Bitte wählen Sie eine Option (1-6): "))
                
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
                    self.programm_beenden()
                else:
                    print("Ungültige Auswahl! Bitte wählen Sie eine Option zwischen 1 und 6.")
            except ValueError:
                print("Fehler: Bitte geben Sie eine gültige Zahl ein.")    self.artikelgruppe_anlegen_bearbeiten()
                elif auswahl == 3:
                    self.wareneingang()
                elif auswahl == 4:
                    self.warenausgang()
                elif auswahl == 5:
                    self.inventarliste_ausgeben()
                elif auswahl == 6:
                    self.programm_beenden()
                else:
                    print("Ungültige Auswahl! Bitte wählen Sie eine Option zwischen 1 und 6.")
            except ValueError:
                print("Fehler: Bitte geben Sie eine gültige Zahl ein.")int("Ungültige Eingabe. Bitte geben Sie die Daten erneut ein.")

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
