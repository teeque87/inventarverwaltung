# Import the Item model and the Database
from model.item import Item
from repo.db import Database


class ItemServices:

    def __init__(self):
        # Initialize the Database as db variable inside the ItemServices class
        self.db = Database()

    def get_one_item(self, product_id: int) -> list[tuple]:
        """
        Retrieves one item from the database based on the provided product ID.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            list[tuple]: A list containing the item details in a tuple if found, 
            otherwise an empty list.

        Raises:
            Exception: If an error occurs while fetching the item from the database.
        """
        try:
            # fetch one item from the database
            item = self.db.fetch_one(product_id)
            product_id, name, amount, cat_id = item
            return (Item(product_id, name, amount, cat_id))
        except Exception as e:
            print(f"Fehler beim Abrufen eines Artikel: {e}")
            return []

    def get_all_items(self) -> list[tuple]:
        """
        Retrieves all items from the database.

        Returns:
            list[tuple]: A list of tuples, each containing details of an item 
            (product_id, name, amount, cat_id).

        Raises:
            Exception: If an error occurs while fetching the items from the database.
        """
        try:
            # fetch all items from the database
            fetched_data = self.db.fetch_all()
            items = [Item(product_id, name, amount, cat_id) for product_id, name, amount, cat_id in fetched_data]
            return items
        except Exception as e:
            print(f"Fehler beim Abrufen aller Artikel: {e}")
            return []

    def get_all_categories(self) -> list[tuple]:
        """
        Retrieves all categories from the database.

        Returns:
            list[tuple]: A list of tuples containing the category data.

        Raises:
            Exception: If an error occurs while fetching the categories from the database.
        """
        try:
            # fetch all categories from the database
            fetched_data = self.db.fetch_all_categories()
            return fetched_data
        except Exception as e:
            print(f"Fehler beim Abrufen aller Kategorien: {e}")
            return []

    def new_category(self, name: str):
        """
        Adds a new category to the database.

        Args:
            name (str): The name of the new category.

        Raises:
            Exception: If an error occurs while adding the new category to the database.
        """
        try:
            # create a new entry for a category
            self.db.add_new_category(name)
            print(f"Kategorie {name} hinzugefügt.")
        except Exception as e:
            print(f"Fehler beim erstellen einer neuen Kategorie: {e}")

    def edit_category(self, cat_id: int, new_name: str):
        """
        Edits an existing category's name in the database.

        Args:
            cat_id (int): The ID of the category to edit.
            new_name (str): The new name for the category.

        Raises:
            Exception: If an error occurs while updating the category in the database.
        """
        try:
            # send a request to the database to update the name for a category
            self.db.edit_category((cat_id, new_name))
            print(f"Kategorie der ID: {cat_id} zu {new_name} geändert.")
        except Exception as e:
            print(f"Fehler beim bearbeiten der Kategorie: {e}")

    def delete_category(self, cat_id: int):
        """
        Deletes a category from the database based on its ID.

        Args:
            cat_id (int): The ID of the category to delete.

        Raises:
            Exception: If an error occurs while deleting the category from the database.
        """
        try:
            # delete a category from the database
            self.db.delete_category(cat_id)
            print(f"Kategorie mit der ID: {cat_id} gelöscht.")
        except Exception as e:
            print(f"Fehler beim löschen einer Kategorie: {e}")

    def delete_item(self, product_id: int):
        """
        Deletes an item from the database based on its product ID.

        Args:
            product_id (int): The ID of the item to delete.

        Raises:
            Exception: If an error occurs while deleting the item from the database.
        """
        try:
            # delete an entry from the database
            self.db.delete_entry(product_id)
            print(f"Artikel mit der ID: {product_id} gelöscht.")
            return True  # wichtig für die Löschung in der InventarGui

        except Exception as e:
            print(f"Fehler beim löschen eines Eintrages: {e}")

    def add_new_item(self, product_id: int, name: str, amount: int, cat_id: int):
        """
        Adds a new item to the database.

        Args:
            product_id (int): The product ID of the new item.
            name (str): The name of the new item.
            amount (int): The quantity of the new item.
            cat_id (int): The category ID the item belongs to.

        Raises:
            Exception: If an error occurs while adding the new item to the database.
        """
        try:
            self.db.add_to_database((product_id, name, amount, cat_id))
            print(
                f"Artikel mit der ID {product_id}, Name {name}, Anzahl {amount}, Kategorie {cat_id} zur Datenbank hinzugefügt.")
        except Exception as e:
            print(f"Fehler beim erstellen eines neuen Artikel: {e}")

    def search_items_id(self, search_term: int) -> list[tuple]:
        """
        Searches for items in the database by product ID.

        Args:
            search_term (int): The product ID to search for.

        Returns:
            list[tuple]: A list of tuples containing the matching items (product_id, name, amount, cat_id).

        Raises:
            Exception: If an error occurs while searching for items by ID.
        """
        try:
            results = self.db.search_by_id(search_term)
            if results:
                items = [Item(product_id, name, amount, cat_id) for product_id, name, amount, cat_id in results]
                return items
        except Exception as e:
            print(f"Fehler beim Abrufen der Artikel: {e}")

    def search_items_name(self, search_term: str) -> list[tuple]:
        """
        Searches for items in the database by name.

        Args:
            search_term (str): The name or part of the name to search for.

        Returns:
            list[tuple]: A list of tuples containing the matching items (product_id, name, amount, cat_id).

        Raises:
            Exception: If an error occurs while searching for items by name.
        """
        try:
            results = self.db.search_by_name(search_term)
            if results:
                items = [Item(product_id, name, amount, cat_id) for product_id, name, amount, cat_id in results]
                return items
        except Exception as e:
            print(f"Fehler beim Abrufen der Artikel: {e}")

    def storage_warning(self) -> bool:
        """
        Checks for items with low stock in the database and prints a warning if any are found.

        Returns:
            bool: True if any items are low in stock, False otherwise.

        Raises:
            Exception: If an error occurs while checking the stock status.
        """
        try:
            results = self.db.check_storage()
            if results:
                items = [Item(product_id, name, amount, cat_id) for product_id, name, amount, cat_id in results]
                print("\n******** WARNUNG ********\nFolgende Artikel sind niedrig im Bestand\n")
                for item in items:
                    print(item)
                return True
            else:
                return False
        except Exception as e:
            print(f"Fehler beim Abrufen des Status: {e}")
            return False

    def add_to_stock(self, product_id: int, amount: int):
        """
        Adds a specified amount to the stock of a product in the database.

        Args:
            product_id (int): The ID of the product to add stock to.
            amount (int): The amount to add to the stock. Must be positive.

        Raises:
            Exception: If an error occurs while updating the stock in the database.
            ValueError: If the provided amount is negative.
        """
        try:
            if amount < 0:
                print("Die Menge muss positiv sein.")
                return

            # fetch the current amount
            item = self.get_one_item(product_id)

            if item:
                new_amount = item.amount + amount
                self.db.update_item_amount(product_id, new_amount)
                print(f"Die Menge des Artikels mit der ID {product_id} wurde um {amount} erhöht.")
            else:
                print("Artikel nicht gefunden.")
        except Exception as e:
            print(f"Fehler beim hinzufügen zum Bestand: {e}")

    def remove_from_stock(self, product_id: int, amount: int):
        """
        Removes a specified amount from the stock of a product in the database.

        Args:
            product_id (int): The ID of the product to remove stock from.
            amount (int): The amount to remove from the stock. Must be positive and less than the current stock.

        Raises:
            Exception: If an error occurs while updating the stock in the database.
            ValueError: If the provided amount is negative or exceeds available stock.
        """
        try:
            if amount < 0:
                print("Die Menge muss positiv sein.")
                return

            # fetch the current amount
            item = self.get_one_item(product_id)

            if item:
                if amount > item.amount:
                    print("Nicht genügend Artikel im Bestand.")
                    return

                new_amount = item.amount - amount
                self.db.update_item_amount(product_id, new_amount)
                print(f"Die Menge des Artikels mit der ID {product_id} wurde um {amount} verringert.")
            else:
                print("Artikel nicht gefunden.")
        except Exception as e:
            print(f"Fehler beim abziehen vom Bestand: {e}")