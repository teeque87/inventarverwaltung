from model.item import Item
from repo.db import Database
import os
import sys


def main():
    item1 = Item(13, "Holzschraube", 350, 3)
    print(item1)



def fetch_one_item(self, product_id):
    item = self.db.fetch_one(product_id)
    item = self.item(item)

    if __name__ == "__main__":
    main()


