import bcrypt
from model.user import User
from repo.db import Database

class UserServices:
    def __init__(self):
         self.db = Database()

    def user_input(self):
        user_name = input("Bitte Benutzernamen eingeben: ")
        user_password = input("Bitte Passwort eingeben: ")
        return user_name,user_password

    def create_user(self, user_name: str, user_password: str):
        # Salt generieren und Passwort hashen
        salt = bcrypt.gensalt(rounds=15)
        hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), salt).decode('utf-8')

        # erzeuht neues Objekt User, wird noch nicht aufgerufen, kann aber für Erweiterungen genutzt werden
        #new_user = User(
            #user_name=user_name,
            #user_password=hashed_password  # Hash als String speichern
            # user_id=user_id,
            #user_role=user_role
        #)
        self.db.add_new_user(user_name, hashed_password)

    def verify_user(self, user_name: str) -> bool:
        user = self.db.get_user_by_username(user_name)

        #if user is None:
            #print("Benutzer nicht gefunden.")
            #return False
        return user is not None

    def verify_password(self, user_name: str,  user_password: str) -> bool:
        user = self.db.get_user_by_username(user_name)
        if user is None:
            print("Benutzer nicht gefunden.")
            return False

        _, password_from_db = user # entpackt das Tupel

        # vergleicht eingegebenes Passwort mit dem in der Datenbank abgelegten Passwort
        if bcrypt.checkpw(user_password.encode('utf-8'), password_from_db.encode('utf-8')):
            print("Erfolgreich eingeloggt.")
            return True
        else:
            print("Login fehlgeschlagen. Überprüfen Sie Ihr Passwort.")
            return False

    def input_user_verification(self):
        user_name, user_password = self.user_input()
        if self.verify_user(user_name):
            return self.verify_password(user_name, user_password)
        else:
            print("Benutzer existiert nicht.")
            return False
        
    def get_all_users(self):
        """Ruft eine Liste aller Benutzer ab."""
        return self.db.get_all_users()

# Beispiel, hinterher rauslöschen
if __name__ == "__main__":

    user_service = UserServices()
    user_name, user_password = user_service.user_input()
    user_service.create_user(user_name, user_password)

    # Benutzerverifikation
    user_service.input_user_verification()