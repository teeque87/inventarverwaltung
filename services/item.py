# Klasse initialisieren
class Item:
  # Klassen-Attribute
    def __init__(self, item_id, name, amount, cat_id): # (min_quantity) Attribut rausgenommen
        self.item_id = item_id
        self.name = name
        self.category = cat_id
        self.amount = amount
        # self.min_quantity = min_quantity -> wird als Datenbankabfrage gelöst
