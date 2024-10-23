import os
from services.item_services import ItemServices

class Menu():
    def __init__(self):
        # initializes the menu with stock warning and ItemServices
        self.stock_warning = False
        self.item_services = ItemServices()
        self.check_storage()
        self.menue_auswahl()

    def check_storage(self):
        # checks whether there is a low stock warning
        self.stock_warning = self.item_services.storage_warning()
        if self.stock_warning:
            input("\nDrücken Sie Enter, um zum Menü zurückzukehren.")

    def clear_console(self):
        # clear console depending on operating system
        os.system('cls' if os.name == 'nt' else 'clear')

    def artikel_suchen(self):
        # item search menu (by ID or name)
        self.clear_console()
        print("\n********** Artikel suchen **********")
        print("1. Nach Artikel-ID suchen")
        print("2. Nach Produktnamen suchen")
        
        try:
            # item search menu (by ID or name)
            auswahl = int(input("\nBitte wählen Sie eine Option (1-2): "))
            
            if auswahl == 1:
                # search by article ID
                search_term = input("\nBitte geben Sie die Artikel-ID ein: ")
                try:
                    # converts the search term into a number (as it is an ID)
                    search_term = int(search_term)  # convert to integer as it is an ID
                except ValueError:
                    # error handling for invalid input
                    print("Ungültige Artikel-ID. Bitte eine Zahl eingeben.")
                    return  # terminates the method if the input is invalid

                results = self.item_services.search_items_id(str(search_term))  # search by article ID

            elif auswahl == 2:
                # search by product name
                search_term = input("\nBitte geben Sie den Produktnamen ein: ")
                results = self.item_services.search_items_name(search_term)  # search by product name

            else:
                # invalid selection (not 1 or 2)
                print("Ungültige Auswahl. Bitte wählen Sie entweder 1 oder 2.")
                return  # terminates the method if the selection is invalid

            # check whether results have been found
            if results:
                print("\nGefundene Artikel:")
                for item in results:
                    print(f"ID: {item.product_id}, Name: {item.name}")
            else:
                print("Keine Artikel gefunden.")
            
        except ValueError:
            # Error handling for invalid number input
            print("Fehler: Bitte geben Sie eine gültige Zahl ein.")
        
        input("\nDrücken Sie Enter, um zum Menü zurückzukehren.")

    # Menu for creating/editing articles
    def artikel_anlegen_bearbeiten(self):
        self.artikel_menue()

    # Submenu for article management (create, edit, delete)
    def artikelgruppe_anlegen_bearbeiten(self):
        self.artikelgr_menue()

    # article Menu
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
                # Select the menu item (1-4)
                auswahl = int(input("Bitte wählen Sie eine Option (1-4): "))
                
                if auswahl == 1:
                    # Create new article
                    self.clear_console()
                    print("\n******** Neuen Artikel anlegen ********\n")
                    try:
                        product_id = int(input("Produkt-ID eingeben: "))
                        name = input("Name des Artikels: ")
                        amount = int(input("Anzahl: "))
                        cat_id = int(input("Kategorie-ID: "))
                        # Adds the new item to the inventory
                        self.item_services.add_new_item(product_id, name, amount, cat_id)
                        input("\nDrücken Sie Enter, um zum Menü zurückzukehren.")
                    except ValueError:
                        # Error handling for invalid input
                        print("Ungültige Eingabe. Bitte geben Sie die Daten erneut ein.")
                elif auswahl == 2:
                    # Edit existing article
                    self.clear_console()
                    print("\n******** Artikel bearbeiten ********")
                    try:
                        # Displays all articles
                        items = self.item_services.get_all_items()
                        for item in items:
                            print(item)
                        # Enter new data for the article
                        product_id = int(input("\nProdukt-ID eingeben: "))
                        name = input("Name des Artikels: ")
                        amount = int(input("Anzahl: "))
                        cat_id = int(input("Kategorie-ID: "))
                        # Updates the item in the inventory
                        self.item_services.add_new_item(product_id, name, amount, cat_id)
                        input("\nDrücken Sie Enter, um zum Menü zurückzukehren.")
                    except ValueError:
                        print("Ungültige Eingabe. Bitte geben Sie die Daten erneut ein.")
                elif auswahl == 3:
                    # Delete article
                    self.clear_console()
                    print("\n******** Artikel löschen ********")
                    try:
                        # Displays all articles
                        items = self.item_services.get_all_items()
                        for item in items:
                            print(item)
                        # Enter the product ID for deletion
                        product_id = int(input("\nProdukt-ID eingeben: "))
                        self.item_services.delete_item(product_id)
                        input("\nDrücken Sie Enter, um zum Menü zurückzukehren.")
                    except ValueError:
                        print("Ungültige Eingabe. Bitte geben Sie die Daten erneut ein.")
                elif auswahl == 4:
                    # Back to the main menu
                    self.clear_console()
                    print("Zurück zum Hauptmenü...")
                    break
                else:
                    # Invalid selection if not 1-4
                    print("Ungültige Auswahl! Bitte wählen Sie eine Option zwischen 1 und 4.")
            except ValueError:
                print("Fehler: Bitte geben Sie eine gültige Zahl ein.")

    # Submenu for article groups (create, edit, delete)
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
                # Select the menu item (1-4)
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
                    # Invalid selection
                    print("Ungültige Auswahl! Bitte wählen Sie eine Option zwischen 1 und 4.")
            except ValueError:
                print("Fehler: Bitte geben Sie eine gültige Zahl ein.")

    # Create new article group
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

    # Edit article group
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

    # Delete article group
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

    # Manage goods receipt
    def wareneingang(self):
        self.clear_console()
        print("\n********** Wareneingang **********")
    
        # articel search
        search_term = input("Bitte geben Sie die Artikel-ID oder den Produktnamen ein: ")
        search_term = self.select_type_for_search(search_term)
        if isinstance(search_term, str):
            results = self.item_services.search_items_name(search_term)
        if isinstance(search_term, int):
            results = self.item_services.search_items_id(search_term)

        # show results
        if results:
            print("\nGefundene Artikel:")
            for item in results:
                print(f"ID: {item.product_id}, Name: {item.name}, Menge: {item.amount}")
            
            # Benutzer zur Eingabe der Menge auffordern
            product_id = int(input("\nBitte geben Sie die Produkt-ID des Artikels ein, den Sie hinzufügen möchten: "))
            amount_to_add = int(input("Bitte geben Sie die Menge ein, die Sie hinzufügen möchten: "))
            
            # Menge hinzufügen
            self.item_services.add_to_stock(product_id, amount_to_add)
            self.check_storage()
        else:
            print("Keine Artikel gefunden.")

        input("\nDrücken Sie Enter, um zum Menü zurückzukehren.")

    # Manage outgoing goods
    def warenausgang(self):
        self.clear_console()
        print("\n********** Warenausgang **********")

        # article search
        search_term = input("Bitte geben Sie die Artikel-ID oder den Produktnamen ein: ")
        search_term = self.select_type_for_search(search_term)
        if isinstance(search_term, str):
            results = self.item_services.search_items_name(search_term)
        if isinstance(search_term, int):
            results = self.item_services.search_items_id(search_term)

        # show results
        if results:
            print("\nGefundene Artikel:")
            for item in results:
                print(f"ID: {item.product_id}, Name: {item.name}, Menge: {item.amount}")
            
            # prompt user to enter the quantity
            product_id = int(input("\nBitte geben Sie die Produkt-ID des Artikels ein, von dem Sie abziehen möchten: "))
            amount_to_remove = int(input("Bitte geben Sie die Menge ein, die Sie abziehen möchten: "))
            
            # subtract quantity
            self.item_services.remove_from_stock(product_id, amount_to_remove)
            self.check_storage()
        else:
            print("Keine Artikel gefunden.")

        input("\nDrücken Sie Enter, um zum Menü zurückzukehren.")

    def select_type_for_search(self, query:str):
        try:
            return int(query)
        except ValueError:
            return query
        

    # Output inventory list
    def inventarliste_ausgeben(self):
        self.clear_console()
        print("********** Aktuell im Bestand **********")
        items = self.item_services.get_all_items()
        for item in items:
            print(item)
        input("\nDrücken Sie Enter, um zum Menü zurückzukehren.")
    
    # Exit program
    def programm_beenden(self):
        print("\n[Programm wird beendet. Auf Wiedersehen!]\n")
        exit()

    # Main menu selection
    def menue_anzeigen(self):
        print("\n********** Inventarverwaltung Hauptmenu **********")
        print("1. Artikel anlegen / bearbeiten")
        print("2. Artikelgruppe anlegen / bearbeiten")
        print("3. Wareneingang")
        print("4. Warenausgang")
        print("5. Inventarliste ausgeben")
        print("6. Artikel suchen")
        print("7. Programm beenden")
        print("**************************************************")

    def menue_auswahl(self):
        while True:
            self.clear_console()
            self.menue_anzeigen()
            try:
                # Select the menu item (1-7)
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
                    self.artikel_suchen()
                elif auswahl == 7:
                    self.programm_beenden()
                else:
                    print("Ungültige Auswahl! Bitte wählen Sie eine Option zwischen 1 und 7.")
            except ValueError:
                print("Fehler: Bitte geben Sie eine gültige Zahl ein.")