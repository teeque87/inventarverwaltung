import sqlite3

class Database():
    __DB_LOCATION = "database.db"

    def __init__(self):
        """initialize db class variables and set cursor"""
        self.connection = sqlite3.connect(Database.__DB_LOCATION)
        self.cur = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def get_all_from_db(self):
        self.cur.execute('''SELECT * FROM articles''')
        return self.cur.fetchall()

    def add_to_database(self, data):
        """add new entry (int: product_id, string: name, int: amount) to the database and replace entry if already exists (product_id)"""
        self.create_table()
        self.cur.executemany('REPLACE INTO articles VALUES(?, ?, ?)', (data,))
        self.connection.commit()

    def create_table(self):
        """create a database table if it does not exist already"""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS articles(product_id integer PRIMARY KEY, name text, amount integer)''')
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