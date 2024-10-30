import streamlit as st
import pandas as pd
from services.item_services import ItemServices

item_services = ItemServices()
items = item_services.storage_warning()

product_ids = []
names = []
amounts = []
categories = []



for item in items:
    product_ids.append(item.product_id)
    names.append(item.name)
    amounts.append(item.amount)
    categories.append(item.category)

df = pd.DataFrame({"product_id": product_ids, "name": names, "amount": amounts, "category": categories})

st.header("Artikel niedrig im Bestand")
st.dataframe(df, column_config={
                "product_id": "Art-Nr",
                "name": "Name",
                "amount": "Menge",
                "category": "Kategorie"
            }, hide_index=True, width=600)