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

    def verify_user(self, user_name: str, user_password: str) -> bool:
        user = self.db.get_user_by_username(user_name) # muss noch implementiert werden

        if user is None:
            print("Benutzer nicht gefunden.")
            return False

        # return bcrypt.checkpw(user_password.encode('utf-8'), user['password'].encode('utf-8'))

        password_from_db = user['password']

        # vergleicht eingegebenes Passwort mit dem in der Datenbank abgelegten Passwort
        password_hashed = bcrypt.hashpw(user_password.encode('utf-8'), password_from_db.encode('utf-8')).decode('utf-8')
        if password_hashed == password_from_db:
            print("Erfolgreich eingeloggt.")
            return True
        else:
            print("Login fehlgeschlagen. Überprüfen Sie Ihr Passwort.")
            return False

    def input_user_verification(self, user_name, user_password):
        #user_name = input("Bitte Benutzernamen eingeben: ")
        #user_password = input("Bitte Passwort eingeben: ")

        if self.verify_user(user_name, user_password):
            print("Login erfolgreich!")
        else:
            print("Login fehlgeschlagen. Überprüfen Sie Ihren Benutzernamen oder Ihr Passwort.")


# Beispiel, hinterher rauslöschen
if __name__ == "__main__":

    user_service = UserServices()
    user = user_service.user_input()
    print(user)
    # Beispiel: Benutzer anlegen
    user_service.input_user_verification(user[0],user[1])

    # Benutzer verifizieren

    #user_service.input_user_verification()