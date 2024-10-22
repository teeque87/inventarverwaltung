# import needed modules
import sqlite3

class Database():
    __DB_LOCATION = "database.db"

    def __init__(self):
        # initialize db class variables and set cursor
        self.connection = sqlite3.connect(Database.__DB_LOCATION)
        self.cur = self.connection.cursor()
        self.__create_table()

    def __del__(self):
        self.connection.close()

    def fetch_all(self) -> list[tuple]:
        """method to get all articles from the database."""
        self.cur.execute('''SELECT product_id, name, amount, cat_name FROM articles LEFT JOIN categories on categories.cat_id = articles.cat_id''')
        return self.cur.fetchall()
    
    def fetch_one(self, product_id: int) -> list[tuple]:
        """method to get one articles from the database. provide an integer as the product_id"""
        self.cur.execute('''SELECT product_id, name, amount, cat_name FROM articles LEFT JOIN categories on categories.cat_id = articles.cat_id WHERE product_id=?''', (product_id,))
        return self.cur.fetchone()
    
    def fetch_all_categories(self) -> list[tuple]: 
        """method to get all categories from the database"""
        self.cur.execute('''SELECT cat_id, cat_name FROM categories''')
        return self.cur.fetchall()

    def add_to_database(self, data: tuple[int, str, int, int]):
        """add new entry (int: product_id, string: name, int: amount, int: cat_id) to the database and replace entry if already exists (product_id)"""
        self.cur.executemany('''REPLACE INTO articles VALUES(?, ?, ?, ?)''', (data,))
        self.connection.commit()

    def add_new_category(self, cat_name: str):
        """add new category (int: cat_id, string: cat_name) to the database and replace categorie if already exists (cat_id)"""
        self.cur.execute('''REPLACE INTO categories VALUES(?, ?)''', (None, cat_name,))
        self.connection.commit()

    def edit_category(self, data: tuple[int, str]):
        """edit a category (int: cat_id, string: cat_name) and write to the database"""
        self.cur.executemany('''REPLACE INTO categories VALUES(?, ?)''', (data,))
        self.connection.commit()

    def delete_category(self, cat_id: int):
        """delete a single category (int: cat_id) from the database"""
        self.cur.execute('''DELETE FROM categories WHERE cat_id = ?''', (cat_id,))
        self.connection.commit()

    def delete_entry(self, product_id: int):
        """delete an entry (int: product_id) from the database"""
        self.cur.execute('''DELETE FROM articles WHERE product_id = ?''', (product_id,))
        self.connection.commit()

    def search_by_id(self, product_id: int) -> list[tuple]:
        """search the database by product_id and returns a list of tuples if an entry or entries are found."""
        self.cur.execute('''SELECT * FROM articles WHERE product_id = ?''', (product_id,))
        return self.cur.fetchall()

    def search_by_name(self, product_name: int) -> list[tuple]:
        """search the database by product_name (name in database) and return a list of tuples if an entry or entries are found."""
        like_pattern = f"%{product_name}%"
        self.cur.execute('''SELECT * FROM articles WHERE name LIKE ?''', (like_pattern,))
        return self.cur.fetchall()

    def check_storage(self, threshold=5) -> list[tuple]:
        """check the database for product that are low on the given (default 5) amount"""
        self.cur.execute('''SELECT * FROM articles WHERE amount <= ?''', (threshold,))
        return self.cur.fetchall()
    
    def update_item_amount(self, product_id: int, new_amount: int):
        """updates the amount by an item in the database given the product_id and the new_amount"""
        self.cur.execute('''UPDATE articles SET amount = ? WHERE product_id = ?''', (new_amount, product_id))
        self.connection.commit()
        
    def __create_table(self):
        """create database tables if it does not exist already"""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS categories(cat_id INTEGER PRIMARY KEY AUTOINCREMENT, cat_name text)''')
        self.connection.commit()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS articles(product_id integer PRIMARY KEY, name text, amount integer, cat_id integer, FOREIGN KEY (cat_id) REFERENCES categories(cat_id))''')
        self.connection.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_value):
        """looking for exceptions before exiting and closing the connection"""
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()
    