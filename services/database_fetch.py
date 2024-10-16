from services.db import Database

# Initialisieren der Datenbank
db = Database()

# abrufen aller Artikel aus Datenbank
all_items = db.get_all_from_db()

# Ergebnisse anzeigen
if all_items:
    print("Gefundene Artikel:")
    for article in all_items:
        product_id, name, amount, category = article
        print(f"Product ID: {product_id}, Name: {name}, Menge: {amount}, Kategorie: {category}")
else:
    print("Keine Artikel in der Datenbank gefunden.")
