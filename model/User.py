class User:
    # Klassen-Attribute
    def __init__(self, user_id, user_name, user_password, user_role):
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role

    def __str__(self):
        return f"User-ID: {self.user_id:8} | Name: {self.user_name:20} | Passwort: {self.user_password:6} | Rolle: {self.user_role}"