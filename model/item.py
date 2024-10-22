
class Item:
    # Klassen-Attribute
    def __init__(self, product_id, name, amount, cat_id):  # (min_quantity) Attribut rausgenommen
        self.product_id = product_id
        self.name = name
        self.category = cat_id
        self.amount = amount

    def __str__(self):
        #print(f"Product ID: {product_id}, Name: {name}, Menge: {amount}, Kategorie: {category}")
        return f"Artikel-ID: {self.product_id:8} | Name: {self.name:20} | Menge: {self.amount:6} | Kategorie: {self.category}"