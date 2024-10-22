from model.item import Item
from repo.db import Database

# initialisiert die ItemServices in einer Datenbankinstan
class ItemServices:

    def __init__(self):
        self.db = Database()

    def get_one_item(self, product_id):
        item = self.db.fetch_one(product_id)
        product_id, name, amount, cat_id = item
        return (Item(product_id, name, amount, cat_id)) #kann durch print ersetzt werden, falls direkte Ausgabe erfolgen soll

    def get_all_items(self):
        try:
            # Daten aus Datenbank abfragen
            fetched_data = self.db.fetch_all()
            items = [Item(product_id, name, amount, cat_id) for product_id, name, amount, cat_id in fetched_data]
            return items

        except Exception as e:
            print(f"Fehler beim Abrufen der Artikel: {e}")
            return []
        
    def get_all_categories(self):
        try:
            # Daten aus Datenbank abfragen
            fetched_data = self.db.fetch_all_categories()
            return fetched_data

        except Exception as e:
            print(f"Fehler beim Abrufen der Artikel: {e}")
            return []
        
    def new_category(self, name):
        self.db.add_new_category(name)
        print(f"Kategorie {name} hinzugefügt.")
    
    def edit_category(self, cat_id, new_name):
        self.db.edit_category((cat_id, new_name))
        print(f"Kategorie der ID: {cat_id} zu {new_name} geändert.")

    def delete_category(self, cat_id):
        self.db.delete_category(cat_id)
        print(f"Kategorie mit der ID: {cat_id} gelöscht.")

    def delete_entry(self, product_id):
        self.db.delete_entry(product_id)
        print(f"Artikel mit der ID: {product_id} gelöscht.")

    def add_new_entry(self, product_id, name, amount, cat_id):
        self.db.add_to_database((product_id, name, amount, cat_id))
        print(f"Artikel mit der ID {product_id}, Name {name}, Anzahl {amount}, Kategorie {cat_id} zur Datenbank hinzugefügt.")

    def search_items_id(self, search_term: str):
        """Sucht in der Datenbank nach Artikeln basierend auf product_id oder name."""
        results = self.db.search_by_id(search_term)
        if results:
            items = [Item(product_id, name, amount, cat_id) for product_id, name, amount, cat_id in results]
            return items

    def search_items_name(self, search_term: str):
        """Sucht in der Datenbank nach Artikeln basierend auf product_id oder name."""
        results = self.db.search_by_name(search_term)
        if results:
            items = [Item(product_id, name, amount, cat_id) for product_id, name, amount, cat_id in results]
            return items
        
    def storage_warning(self) -> bool:
        results = self.db.check_storage()
        if results:
            items = [Item(product_id, name, amount, cat_id) for product_id, name, amount, cat_id in results]
            print("\n******** WARNUNG ********\nFolgende Artikel sind niedrig im Bestand\n")
            for item in items:
                print(item)
            return True
        else:
            return False
    

    def add_to_stock(self, product_id: int, amount: int):
        """Erhöht die Menge eines Artikels in der Datenbank um den angegebenen Betrag."""
        if amount < 0:
            print("Die Menge muss positiv sein.")
            return

        # Den aktuellen Artikel abrufen
        item = self.get_one_item(product_id)
        
        if item:
            new_amount = item.amount + amount
            self.db.update_item_amount(product_id, new_amount)
            print(f"Die Menge des Artikels mit der ID {product_id} wurde um {amount} erhöht.")
        else:
            print("Artikel nicht gefunden.")

    
    def remove_from_stock(self, product_id: int, amount: int):
        """Verringert die Menge eines Artikels in der Datenbank um den angegebenen Betrag."""
        if amount < 0:
            print("Die Menge muss positiv sein.")
            return

        # Den aktuellen Artikel abrufen
        item = self.get_one_item(product_id)
        
        if item:
            if amount > item.amount:
                print("Nicht genügend Artikel im Bestand.")
                return
            
            new_amount = item.amount - amount
            self.db.update_item_amount(product_id, new_amount)
            print(f"Die Menge des Artikels mit der ID {product_id} wurde um {amount} verringert.")
        else:
            print("Artikel nicht gefunden.")