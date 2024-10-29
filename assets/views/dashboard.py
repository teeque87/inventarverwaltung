import streamlit as st
import pandas as pd
from services.item_services import ItemServices


item_services = ItemServices()
items = item_services.get_all_items()
cats = item_services.get_all_categories()


product_ids = []
names = []
amounts = []
categories = []

@st.dialog("Artikel bearbeiten")
def edit_item(selected_index):
    selected_data = df.iloc[selected_index]
    
    _cats = []
    _catindex = 0

    for cat in cats:
        _cats.append(cat[1])

    if selected_data.iloc[3] is not None:
        _catindex = _cats.index(selected_data.iloc[3])

    _product_id = st.text_input("Artikelnummer", selected_data.iloc[0], disabled=True)
    _name = st.text_input("Produktname", selected_data.iloc[1])
    _amount = st.text_input("Menge", selected_data.iloc[2])
    _category = st.selectbox("Kategorien: ", _cats, index=_catindex)
    col1_, col2_ = st.columns([1,1])
    with col1_:
        if st.button("Speichern"):
            _cat = _cats.index(_category) + 1
            item_services.add_new_item(_product_id, _name, _amount, _cat)
            st.rerun()
    with col2_:
        if st.button("Abbrechen"):
            st.rerun()
    

for item in items:
    product_ids.append(item.product_id)
    names.append(item.name)
    amounts.append(item.amount)
    categories.append(item.category)

df = pd.DataFrame({"product_id": product_ids, "name": names, "amount": amounts, "category": categories})


st.header("Artikelübersicht")
st.dataframe(df, column_config={
                "product_id": "Art-Nr",
                "name": "Name",
                "amount": "Menge",
                "category": "Kategorie"
            }, hide_index=True, use_container_width=True)

# Selectbox formatting and checking if something has been selected
row_details = [f"{row['product_id']:10} - {row['name']:10} - Menge: {row['amount']:10} - Kategorie: {row['category']}" for _, row in df.iterrows()]
row_details = ["Bitte wählen..."] + row_details
selected_item = st.selectbox("Wähle einen Datensatz der bearbeitet werden soll:", row_details)
selected_index = row_details.index(selected_item)
if selected_item != "Bitte wählen...":
    edit_item(selected_index - 1)

# Count items for the bar chart and display
category_counts = df["category"].value_counts().reset_index()
category_counts.columns = ["Kategorie", "Anzahl"]

st.bar_chart(category_counts.set_index("Kategorie"))