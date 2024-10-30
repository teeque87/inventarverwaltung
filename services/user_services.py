import bcrypt
from model.user import User
from repo.db import Database

class UserServices:
    """
       A class for managing user authentication and verification.

       Methods:
           __init__(self): Initializes a UserServices instance with a database connection.
           create_user(self, user_name: str, user_password: str): Creates a new user by hashing the password
               and storing the username and hashed password in the database.
           verify_password(self, user_name: str, user_password: str) -> bool: Verifies whether the given
               password matches the hashed password stored in the database for the specified username.
               Returns True if the password is correct, otherwise False.

       Dependencies:
           bcrypt: Library for password hashing and verification.
           User: Represents a user model.
           View: Graphical User Interface used CLI and GUI (tkinter and Streamlit)
           Database: Provides methods for interacting with the user database (used database SQLite3)

       Example:
           user_services = UserServices()
           user_services.create_user("username", "password")
           user_services.input_user_verification()
       """

    def __init__(self):
        """Initializes the UserServices instance and establishes a database connection."""
        self.db = Database()

    def create_user(self, user_name: str, user_password: str):
        """
               Creates a new user by hashing the password and storing it in the database.

               Param:
                   user_name (str): The username for the new user.
                   user_password (str): The password for the new user.
               """
        salt = bcrypt.gensalt(rounds=15)
        hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), salt).decode('utf-8')
        self.db.add_new_user(user_name, hashed_password)

    def verify_password(self, user_name: str,  user_password: str) -> bool:
        """
               Verifies the entered password against the hashed password stored in the database.

               Param:
                   user_name (str): The user's username.
                   user_password (str): The password to be verified.

               Returns:
                   bool: True if the password is correct, otherwise False.
               """
        user = self.db.get_user_by_username(user_name)
        if user is None:
            print("Benutzer nicht gefunden.")
            return False

        _, password_from_db = user # entpackt das Tupel

        if bcrypt.checkpw(user_password.encode('utf-8'), password_from_db.encode('utf-8')):
            print("Erfolgreich eingeloggt.")
            return True
        else:
            print("Login fehlgeschlagen. Überprüfen Sie Ihr Passwort.")
            return False