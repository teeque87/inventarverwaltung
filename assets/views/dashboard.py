import streamlit as st
import pandas as pd
from services.item_services import ItemServices

# Initialize used services and get data from the database
item_services = ItemServices()
items = item_services.get_all_items()
cats = item_services.get_all_categories()


# Function to show a dialog to edit an item
@st.dialog("Artikel bearbeiten")
def edit_item(selected_index):
    selected_data = df.iloc[selected_index]
    
    # Iterate through the categories to get the names to populate the selectbox
    _cats = []
    _catindex = 0

    for cat in cats:
        _cats.append(cat[1])

    # Prepopulate the category if one is set
    if selected_data.iloc[3] is not None:
        _catindex = _cats.index(selected_data.iloc[3])

    # Define all the text input fields with their prefilled values
    _product_id = st.text_input("Artikelnummer", selected_data.iloc[0], disabled=True)
    _name = st.text_input("Produktname", selected_data.iloc[1])
    _amount = st.text_input("Menge", selected_data.iloc[2])
    _category = st.selectbox("Kategorien: ", _cats, index=_catindex)
    if st.button("Speichern", key="save"):
        _categories = item_services.get_all_categories()
        for _id_cat, _name in _categories:
            if _name == _category:
                item_services.add_new_item(_product_id, _name, _amount, _id_cat)
                st.rerun()

# Function to open a dialog to confirm deletion
@st.dialog("Wirklich löschen?")
def delete_item(_id, action):
    if action == "product":
        st.write(f"Artikel mit Artikelnummer: {_id} wirklich löschen?")
        if st.button("Bestätigen", key="confirm_delete"):
            item_services.delete_item(_id)
            st.rerun()
    if action == "category":
        st.write(f"Kategorie mit der ID: {_id} wirklich löschen?")
        if st.button("Bestätigen", key="confirm_delete"):
            item_services.delete_category(_id)
            st.rerun()

product_ids = []
names = []
amounts = []
categories = []    

# Fill the empty arrays with each corresponding attributes from the database tuple array
for item in items:
    product_ids.append(item.product_id)
    names.append(item.name)
    amounts.append(item.amount)
    categories.append(item.category)

# Insert the arrays into the dictionary value fields of each matching key pair
df = pd.DataFrame({"product_id": product_ids, "name": names, "amount": amounts, "category": categories})


st.header("Artikelübersicht")
# Display the Table with all Data
st.dataframe(df, column_config={
                "product_id": "Art-Nr",
                "name": "Name",
                "amount": "Menge",
                "category": "Kategorie"
            }, hide_index=True, use_container_width=True)




st.sidebar.title("Artikel")
action = st.sidebar.selectbox("Wähle eine Aktion:", ["Artikel bearbeiten", "Artikel erstellen", "Artikel löschen", "Statistiken"])

if action == "Artikel bearbeiten":
    # Display a selectbox, formatting and checking if something has been selected
    row_details = [f"{row['product_id']:10} - {row['name']:10} - Menge: {row['amount']:10} - Kategorie: {row['category']}" for _, row in df.iterrows()]
    row_details = ["Bitte wählen..."] + row_details
    selected_item = st.selectbox("Wähle einen Datensatz der bearbeitet werden soll:", row_details)
    selected_index = row_details.index(selected_item)
    if selected_item != "Bitte wählen...":
        edit_item(selected_index - 1)

elif action == "Artikel erstellen":
    # Iterate through the categories to get the names to populate the selectbox
    _cats = []
    _catindex = 0

    for cat in cats:
        _cats.append(cat[1])
    
    sum_of_articles = len(product_ids) + 1

    # Define all the text input fields with their prefilled values
    _product_id = st.text_input("Artikelnummer", value=sum_of_articles)
    _name = st.text_input("Produktname")
    _amount = st.text_input("Menge")
    _category = st.selectbox("Kategorien: ", _cats, index=_catindex)
    
    if st.button("Speichern", key="save_new") and _product_id != "" and _name != "" and _amount != "":
        _categories = item_services.get_all_categories()
        for _id_cat, _cat_name in _categories:
            if _cat_name == _category:
                # Save the new values from the textboxes to the database
                item_services.add_new_item(_product_id, _name, _amount, _id_cat)
                st.rerun()

elif action == "Artikel löschen":
    st.subheader("Artikel löschen")
    _product_id = st.text_input("Artikelnummer")
    if st.button("Löschen", key="delete"):
        delete_item(_product_id, "product")


elif action == "Statistiken":
    col1, col2 = st.columns(2)

    # Count items for the bar chart and display it
    with col1:
        category_counts = df["category"].value_counts().reset_index()
        category_counts.columns = ["Kategorie", "Anzahl"]

        st.bar_chart(category_counts.set_index("Kategorie"))

    with col2:
        amount_of_articles = len(product_ids)
        st.metric("Artikel", amount_of_articles)

        total_amount = 0
        for i in amounts:
            total_amount = total_amount + i
        st.metric("Lagerbestand", total_amount)

st.sidebar.title("Kategorien")
action_cat = st.sidebar.selectbox("Wähle eine Aktion:", ["Bitte Wählen...", "Kategorie anlegen", "Kategorie bearbeiten", "Kategorie löschen"])

if action_cat == "Bitte Wählen...":
    pass

if action_cat == "Kategorie anlegen":
    st.subheader("Kategorie anlegen")
    cat_input = st.text_input("Name der Kategorie")
    if st.button("Hinzufügen") and cat_input != "":
        item_services.new_category(cat_input)

elif action_cat == "Kategorie bearbeiten":
    st.subheader("Kategorie bearbeiten")
    _categories = item_services.get_all_categories()
    st.dataframe(_categories, use_container_width=True, hide_index=True, column_config={"0": "ID", "1": "Name"})
    _id = st.text_input("ID der Kategorie")
    for cat in _categories:
        try:
            _id = int(_id)
            if cat[0] == _id:
                _index = next((i for i, cat in enumerate(_categories) if cat[0] == _id), None)
                _new_name = st.text_input("Neuer Name", value=_categories[_index][1])
                if st.button("Aktualisieren", key="edit_cat"):
                    item_services.edit_category(_id, _new_name)
                    st.rerun()
        except ValueError:
            st.rerun()

elif action_cat == "Kategorie löschen":
    st.subheader("Kategorie löschen")
    _cats = []
    _catindex = 0

    for cat in cats:
        _cats.append(cat[1])
    
    _category = st.selectbox("Kategorien: ", _cats, index=_catindex)
    if st.button("Löschen", key="delete_cat"):
        _categories = item_services.get_all_categories()
        for _id, _name in _categories:
            if _name == _category:
                delete_item(_id, "category")