import services.item_services
import logging

# Erstelle die Datenbank-Instanz einmal, um sie von außen übergeben zu können
db_instance = Database()  # Erstelle die Datenbank-Instanz einmal
item_service = ItemServices(db_instance)
