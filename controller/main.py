from model.item import Item
from services.item_services import ItemServices

def main():
    item1 = Item(13, "Holzschraube", 350, 3)
    print(item1)

if __name__ == "__main__":
    main()

# Erstelle die Datenbank-Instanz einmal, um sie dann von außen übergeben zu können
db_instance = Database()  # Erstelle die Datenbank-Instanz einmal
item_service = ItemServices(db_instance)
