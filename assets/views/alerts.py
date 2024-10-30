import streamlit as st
import pandas as pd
from services.item_services import ItemServices

# Initialize the ItemServices to manage items
item_services = ItemServices()

# Get items that have a low stock warning
items = item_services.storage_warning()

# Initialize lists to store product details
product_ids = []
names = []
amounts = []
categories = []


# Iterate over the items to extract product details
for item in items:
    product_ids.append(item.product_id) # Collect product IDs
    names.append(item.name)             # Collect item names
    amounts.append(item.amount)         # Collect item amounts
    categories.append(item.category)    # Collect item categories

# Create a DataFrame from the collected item details
df = pd.DataFrame({"product_id": product_ids, "name": names, "amount": amounts, "category": categories})

# Set the header for the Streamlit app
st.header("🚨 Artikel niedrig im Bestand")

# Display the DataFrame as a table in the Streamlit app
st.dataframe(df, column_config={
                "product_id": "Art-Nr",         # Column for product ID
                "name": "Name",                 # Column for item name
                "amount": "Menge",              # Column for item amount
                "category": "Kategorie"         # Column for item category
            }, hide_index=True, width=600)