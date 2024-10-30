import hmac
import streamlit as st
 
st.set_page_config(
    page_title="Inventarverwaltungssystem",
    page_icon="👋",
)

def check_password():
    """Returns `True` if the user had a correct password."""
 
    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)
 
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        username = st.session_state.get("username")
        password = st.session_state.get("password")
        
        # Check if username and password are correct
        if username in st.secrets["passwords"] and hmac.compare_digest(
            password,
            st.secrets.passwords[username],
        ):
            st.session_state["password_correct"] = True
            # Clear sensitive information
            del st.session_state["password"]
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False
 
    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True
 
    # Show inputs for username and password.
    login_form()
    if st.session_state.get("password_correct") is False:
        st.error("😕 User not known or password incorrect")
    return False
 
if not check_password():
    st.stop()

# Main application content

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")
dashboard = st.Page(
    "reports/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True
)
st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
