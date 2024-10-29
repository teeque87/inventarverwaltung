from services.item_services import ItemServices

item_services = ItemServices()

categories = [
    'Werkzeuge',
    'Baustoffe',
    'Farben',
    'Elektro',
    'Garten'
]

articles = [
    (1, 'Hammer', 50, 1),          # Produkt ID, Name, Menge, Kategorie ID
    (2, 'Schraubenzieher', 100, 1), 
    (3, 'Zement', 200, 2),         
    (4, 'Ziegelstein', 500, 2),    
    (5, 'Wandfarbe Weiß', 150, 3), 
    (6, 'Lackfarbe Blau', 80, 3),  
    (7, 'Kabelrolle', 75, 4),      
    (8, 'Steckdose', 120, 4),      
    (9, 'Rasenmäher', 20, 5),      
    (10, 'Gartenschere', 60, 5)    
]

for cat in categories:
    #item_services.new_category(cat)
    pass # löschen

for art in articles:
    product_id, name, amount, cat_id = art
    #item_services.add_new_item(product_id, name, amount, cat_id)