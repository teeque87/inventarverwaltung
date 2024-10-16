import os
import sys
# insert root directory into python module search path
sys.path.insert(1, os.getcwd())

from model.item import Item
from repo.db import Database

class ItemServices:

    def __init__(self):
        self.db = Database()

    def fetch_one_item(self, product_id):
        item = self.db.fetch_one(product_id)
        product_id, name, amount, cat_id = item
        print(Item(product_id, name, amount, cat_id))

    def fetch_all_items(self):
        fetched_data = self.db.fetch_all()
        for item in fetched_data:
            product_id, name, amount, cat_id = item
            print(Item(product_id, name, amount, cat_id))
        