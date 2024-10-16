# import needed modules
import sqlite3

class Database():
    __DB_LOCATION = "database.db"

    def __init__(self):
        # initialize db class variables and set cursor
        self.connection = sqlite3.connect(Database.__DB_LOCATION)
        self.cur = self.connection.cursor()
        self.create_table()

    def __del__(self):
        self.connection.close()

    def get_all_from_db(self) -> tuple[int, str, int, str]:
        """method to get all articles from the database"""
        self.cur.execute('''SELECT product_id, name, amount, cat_name FROM articles INNER JOIN categories on categories.cat_id = articles.cat_id''')
        return self.cur.fetchall()

    def add_to_database(self, data: tuple[int, str, int, int]):
        """add new entry (int: product_id, string: name, int: amount, int: cat_id) to the database and replace entry if already exists (product_id)"""
        self.cur.executemany('REPLACE INTO articles VALUES(?, ?, ?)', (data,))
        self.connection.commit()

    def add_new_category(self, data: tuple[int, str]):
        """add new category (int: cat_id, string: cat_name) to the database and replace categorie if already exists (cat_id)"""
        self.cur.executemany('REPLACE INTO categories VALUES(?, ?)', (data,))
        self.connection.commit()

    def create_table(self):
        """create a database table if it does not exist already"""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS categories(cat_id integer PRIMARY KEY, cat_name text)''')
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