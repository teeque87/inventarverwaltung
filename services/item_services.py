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
    
    def edit_category(self, cat_id, new_name):
        self.db.edit_category((cat_id, new_name))

    def delete_category(self, cat_id):
        self.db.delete_category(cat_id)

    def add_new_entry(self, product_id, name, amount, cat_id):
        self.db.add_to_database((product_id, name, amount, cat_id))