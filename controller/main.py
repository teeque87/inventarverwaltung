from model.item import Item
from services.item_services import ItemRepository
from services.item_services import ItemServices
from repo.db import Database
import logging


def main():
    product_id = 1 # Eingabe aus UI

    # Erstelle die Datenbank-Instanz einmal, um sie dann von außen übergeben zu können
    db_instance = Database()  # Erstelle die Datenbank-Instanz einmal
    item_repository = ItemRepository(db_instance)

    item_services =  ItemServices(item_repository)
    all_items = item_services.fetch_all_items()
    one_item = item_services.fetch_one_item(product_id) # für Einzelartikel-Ausgabe - UI Eingabe+Verknüpfung
    for item in all_items:
        print(item)



if __name__ == "__main__":
    main()


