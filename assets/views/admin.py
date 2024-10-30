import streamlit as st
from services.user_services import UserServices
import bcrypt

st.title("🚨Benutzerverwaltung")
user_services = UserServices()

st.sidebar.title("Benutzer verwalten")
action = st.sidebar.selectbox("Wähle eine Aktion:", ["Benutzer erstellen", "Benutzer löschen", "Benutzerpasswort bearbeiten","Alle Benutzer anzeigen"])

if action == "Benutzer erstellen":
    st.subheader("Neuen Benutzer erstellen")
    user_name = st.text_input("Benutzername:")
    user_password = st.text_input("Passwort:", type="password")
    confirm_password = st.text_input("Passwort bestätigen:", type="password")
    
    if st.button("Benutzer erstellen"):
        if user_name and user_password and user_password == confirm_password:
            user_services.create_user(user_name, user_password)
            st.success(f"Benutzer '{user_name}' wurde erfolgreich erstellt.")
        else:
            st.error("Bitte stellen Sie sicher, dass alle Felder ausgefüllt sind und die Passwörter übereinstimmen.")

elif action == "Benutzer löschen":
    st.subheader("Benutzer löschen")
    user_name = st.text_input("Benutzername des zu löschenden Benutzers:")
    
    if st.button("Benutzer löschen"):
        if user_services.verify_user(user_name):
            if st.confirm("Sind Sie sicher, dass Sie diesen Benutzer löschen möchten?"):
                user_services.db.delete_user(user_name)
                st.success(f"Benutzer '{user_name}' wurde erfolgreich gelöscht.")
            else:
                st.info("Löschvorgang abgebrochen.")
        else:
            st.error("Benutzer wurde nicht gefunden.")
elif action == "Benutzerpasswort bearbeiten":
    st.subheader("Passwort eines Benutzers bearbeiten")
    user_name = st.text_input("Benutzername des zu bearbeitenden Benutzers:")
    new_password = st.text_input("Neues Passwort:", type="password")
    confirm_new_password = st.text_input("Neues Passwort bestätigen:", type="password")
    
    if st.button("Passwort ändern"):
        if user_services.verify_user(user_name):
            if new_password and new_password == confirm_new_password:
                # Passwort hashen und aktualisieren
                hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                user_services.db.update_user_password(user_name, hashed_password)
                st.success(f"Passwort für Benutzer '{user_name}' wurde erfolgreich aktualisiert.")
            else:
                st.error("Bitte geben Sie ein neues Passwort ein und stellen Sie sicher, dass die Passwörter übereinstimmen.")
        else:
            st.error("Benutzer wurde nicht gefunden.")
elif action == "Alle Benutzer anzeigen":
    st.subheader("Alle Benutzer")
    users = user_services.get_all_users()
    if users:
        for user in users:
            st.write(user[1])  # Zeigt den Benutzernamen an
    else:
        st.write("Keine Benutzer gefunden.")