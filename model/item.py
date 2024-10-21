
class Item:
    # Klassen-Attribute
    def __init__(self, product_id, name, amount, cat_id):  # (min_quantity) Attribut rausgenommen
        self.product_id = product_id
        self.name = name
        self.category = cat_id
        self.amount = amount
        # self.min_quantity = min_quantity -> wird als Datenbankabfrage gelöst


    def __str__(self):
        #print(f"Product ID: {product_id}, Name: {name}, Menge: {amount}, Kategorie: {category}")
        return f"Artikel-ID: {self.product_id:10} | Name: {self.name:10} | Menge: {self.amount:10} | Kategorie: {self.category}"