from model.item import Item
from repo.db import Database


# diese Klasse stellt alle Services zur Verwaltung der Artikel bereit
class ItemServices:

    def __init__(self):
        self.db = Database()

    def fetch_one_item(self, product_id):
        item = self.db.fetch_one(product_id)
        product_id, name, amount, cat_id = item
        return (Item(product_id, name, amount, cat_id)) #kann durch print ersetzt werden, falls direkte Ausgabe rfolgen soll
        #return item

    def fetch_all_items(self):
        try:
            # Daten aus Datenbank abfragen
            fetched_data = self.db.fetch_all()

            # Liste von Artikeln anlegen und zurückgeben
            items = [Item(product_id, name, amount, cat_id) for product_id, name, amount, cat_id in fetched_data]
            return items


        except Exception as e:
            print(f"Fehler beim Abrufen der Artikel: {e}")
            # [] wird bei Fehler zurückgegeben
            return []

    def add_new_item(self, product_id, name, amount, cat_id):
        data = (product_id, name, amount, cat_id)
        self.db.add_to_database(data)
        #product_id, name, amount, cat_id = data
        print(f'Artikel {name} mit Produkt-ID {product_id} wurde der Datenbank hinzugefügt.')


    def add_new_category(self, cat_name):
        self.db.add_new_category(cat_name)
        print(f'Artikelgruppe "{cat_name}" wurde der Datenbank hinzugefügt.')

