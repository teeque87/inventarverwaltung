from model.item import Item
from repo.db import Database

# initialisiert die ItemServices in einer Datenbankinstanz
class ItemRepository:
    def __init__(self, db: Database):
        self.db = db  #Instanz der Klasse Database zur Datenbankinteraktion

    #try:
        #self.db = sqlite3.connect(Database)
        #print("Erfolgreich mit der Datenbank verbunden!")
    #except sqlite3.OperationalError as e:
        #print(f"Fehler beim Verbinden mit der Datenbank: {e}")
    #except sqlite3.Error as e:
        #print(f"Allgemeiner Datenbankfehler: {e}")

# diese Klasse stellt alle Services zur Verwaltung der Artikel bereit
class ItemServices:

    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def fetch_one_item(self, product_id):
        item = self.repository.db.fetch_one(product_id)
        product_id, name, amount, cat_id = item
        print(Item(product_id, name, amount, cat_id))

    def fetch_all_items(self):
        try:
            # Daten aus Datenbank abfragen
            fetched_data = self.repository.db.fetch_all()

            # Liste von Artikeln anlegen und zurückgeben
            items = [Item(product_id, name, amount, cat_id) for product_id, name, amount, cat_id in fetched_data]
            return items
            #return fetched_data

        except Exception as e:
            print(f"Fehler beim Abrufen der Artikel: {e}")
            # None wird bei Fehler zurückgegeben
            return None
