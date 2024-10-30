import streamlit as st
from services.user_services import UserServices

st.set_page_config(
    page_title="Inventarverwaltungssystem",
    page_icon="👋",
)

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''

st.markdown(hide_img_fs, unsafe_allow_html=True)


def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        st.image("assets/images/logo.png")
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        user_services = UserServices()
        is_valid = user_services.verify_password(st.session_state["username"], st.session_state["password"])
        if is_valid:
            st.session_state["logged_in"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["logged_in"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("logged_in", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "logged_in" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()


# Logged in Content

#Pages
dashboard = st.Page("assets/views/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True)
alerts = st.Page("assets/views/alerts.py", title="Bestandswarnung", icon=":material/notification_important:")
admin_page = st.Page("assets/views/admin.py", title="Adminpanel", icon=":material/notification_important:")


if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [admin_page],
            "Reports": [dashboard, alerts]
        }
    )
    pg.run()