<<<<<<< HEAD


=======
from model.item import Item
from repo.db import Database

# initialisiert die ItemServices in einer Datenbankinstanz
class ItemRepository:
    def __init__(self, db: Database):
        self.db = db  #Instanz der Klasse Database zur Datenbankinteraktion
        # gibt es einen try/except Block in der Datenbank?

# diese Klasse stellt alle Services zur Verwaltung der Artikel bereit
class ItemServices:

    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def fetch_one_item(self, product_id):
        item = self.repository.db.fetch_one(product_id)
        product_id, name, amount, cat_id = item
        return (Item(product_id, name, amount, cat_id)) #kann durch print ersetzt werden, falls direkte Ausgabe rfolgen soll
        #return item

    def fetch_all_items(self):
        try:
            # Daten aus Datenbank abfragen
            fetched_data = self.repository.db.fetch_all()

            # Liste von Artikeln anlegen und zurückgeben
            items = [Item(product_id, name, amount, cat_id) for product_id, name, amount, cat_id in fetched_data]
            return items


        except Exception as e:
            print(f"Fehler beim Abrufen der Artikel: {e}")
            # [] wird bei Fehler zurückgegeben
            return []
>>>>>>> origin/isa
