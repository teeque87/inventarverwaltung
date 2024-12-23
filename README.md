![enter image description here](https://tse1.mm.bing.net/th?id=OIG4.k5fL_MZmyAwPGwWDYhMZ&pid=ImgGn)

# Inventory Management System

This Inventory Management System is a versatile application built in Python for efficient stock and product group management, available as a Command Line Interface (CLI) and a Graphical User Interface (GUI) with Tkinter and Streamlit. It simplifies inventory control with functionalities for adding, editing, and deleting items, managing stock levels and providing low-stock alerts.  

With quick search options, category management, and user-friendly navigation, this system aims to streamline inventory operations for businesses and personal use. Installation is straightforward, and the application supports both terminal and GUI interaction. Future enhancements will include reporting and export features to improve data accessibility and analytics.

# Inventory Management System (Version with CLI)

## **Overview**

This Inventory Management System is a Python-based application designed for efficient management of products, product groups, and stock levels.  
It offers functionalities for adding, editing, and deleting items and item groups, as well as managing incoming and outgoing stock movements.  
Additionally, the system provides low stock alerts and enables quick item search.

## **Features**

- **Add/Edit/Delete Items:** Manage individual items in the inventory by adding, editing, or deleting them.
- **Create/Edit/Delete Item Groups:** Categorize items into groups and manage them efficiently.
- **Inventory Management:** Easily handle incoming stock (increase inventory) and outgoing stock (decrease inventory).
- **Stock Alert:** Receive alerts when stock levels fall below a critical threshold.
- **Item Search:** Quickly locate items by searching by item ID or product name.
- **Display Inventory List:** View a list of all items currently in stock.

## Technologies Used

- **Python**: The programming language used for this project.
- **SQLite**: The database used to store inventory data.
- **ItemServices**: A custom module handling operations related to items and stock.
- **Terminal-based User Interface**: Runs in the console, interacting through text-based input and output.
- **GUI with Tkinter**: Offers a graphical user interface where input fields and controls allow user interaction with inventory operations and a display of results through GUI elements.

## **Getting Started**


### Prerequisites

Ensure `Python` is installed on your system. Check the Python version with:
```
python --version
```

### Installation

Clone the repository:
```
git clone https://github.com/teeque87/inventarverwaltung.git
```
Navigate to the project directory:
```
cd inventarverwaltungssystem
```
Install dependencies (ideally in a virtual environment such as venv or Anaconda):
```
pip install tk
pip install bcrypt
pip install streamlit
```
To launch the application, use one of the following commands depending on your operating system:
```
python main.py
```
```
python3 main.py
```
To start the web application, run the following command in the main directory:
```
streamlit run Inventarverwaltung.py
```
Once the application starts, the main menu appears in your terminal, offering options such as:

### Main Menu

- **Add / Edit Items**
    - **Submenu: Item Management**
        - Add Item
        - Edit Item
        - Delete Item
        - Return to Main Menu
- **Add / Edit Item Group**
    - **Submenu: Item Group Management**
        - Add Item Group
        - Edit Item Group
        - Delete Item Group
        - Return to Main Menu
- **Incoming Stock**
    - Searches for an item and allows entering the quantity to be added.
- **Outgoing Stock**
    - Searches for an item and allows entering the quantity to be deducted.
- **Display Inventory List**
    - Shows a list of all items currently in stock.
- **Search Item**
    - **Submenu: Item Search**
        - Search by Item ID
        - Search by Product Name
- **Exit Program**
    - Closes the program.

Follow the on-screen instructions to manage the inventory as needed.

## **Future Improvements**

Add reporting and export functions (e.g., CSV or PDF reports).

# Inventory Management System Version with GUI (Tkinter)

This project is an **Inventory Management System** with a graphical user interface (GUI) built with Python and the Tkinter framework. It allows inventory management through adding, editing, deleting, and searching for items and provides an overview of the entire inventory.

## Features

- **Add Item**: Enables adding new items to the inventory.
- **Edit Item**: Edit existing items based on their ID.
- **Delete Item**: Delete items from the inventory.
- **Search Item**: Search for items by their ID or name.
- **Display Inventory List**: Shows a list of all items in the inventory.
- **GUI-based Navigation**: User-friendly graphical interface with a main menu and various input forms.

## **Future Improvements**

Add reporting and export functions (e.g., CSV or PDF reports) and managing and display outcoming and incoming stock. Further user and account management.



# Inventory Management System Version with GUI (streamlit)

This project is an **Inventory Management System** with a graphical user interface (GUI) built with Python and the streamlit framework. It allows inventory management through adding, editing, deleting, and searching for items and provides an overview of the entire inventory.

## Features

- **Add Item**: Enables adding new items to the inventory.
- **Edit Item**: Edit existing items based on their ID.
- **Delete Item**: Delete items from the inventory.
- **Search Item**: Search for items by their ID or name.
- **Display Inventory List**: Shows a list of all items in the inventory.
- **User Authentication
- **GUI-based Navigation**: User-friendly graphical interface with a main menu and various input forms.

# Inventory Management System with User Authentication (only available in the streamlit Version)

This Inventory Management System includes a user authentication feature to support multiple users, secure login, and personalized access to inventory management functions. Passwords are securely hashed before storage, ensuring data integrity and user privacy. 

## **Features**

- **Multi-User Support**: Allows different users to create individual accounts, each with unique login credentials.
- **Secure Login**: Users are authenticated via a secure login process with passwords that are hashed using bcrypt before storage, protecting them from unauthorized access.
- **Password Hashing**: During registration, user passwords are hashed using bcrypt, a strong cryptographic hashing library. Hashed passwords are then stored in the database, meaning actual passwords are never saved, adding a layer of security.
- **User-Specific Access**: Each user logs in with their own credentials, which helps maintain personal account integrity and allows user-specific features or settings in future iterations.

## **Getting Started with User Accounts**

1. **Create a New User**: 
    - On first run, a new user can create an account by entering a username and password. The password is then hashed and stored securely in the database.

2. **Log In as Existing User**: 
    - If an account already exists, the user can log in by entering their username and password. The system verifies the password by comparing the hashed version of the input with the stored hash in the database.

3. **Manage User Sessions**: 
    - Upon successful login, users can access inventory management functions such as adding, editing, deleting items, and viewing inventory lists.

## **Technology Used for Authentication**

- **bcrypt**: A cryptographic library used to hash and verify passwords securely.
- **SQLite**: Database used to store user data, including hashed passwords, securely and reliably.

This feature-rich system provides not only efficient inventory management but also strong user authentication, making it suitable for business environments with multiple users and sensitive data requirements.

## Requirements

To run this project, you need:

- **Python 3.x**
- **Tkinter** (install through package manager)
- **bcrypt** (install through package manager)
- **streamlit** 

### Main Menu

Upon starting the application, the main menu is displayed. From here, you can perform the following actions:

1. **Search Item by ID**: Search for an item by its ID and display details.
2. **Search Item by Name**: Search for an item by its name.
3. **Add Item**: Add a new item to the inventory by entering the ID, name, quantity, and category ID.
4. **Edit Item**: Modify details of an existing item by entering the item ID and updating relevant fields.
5. **Delete Item**: Delete an item from the inventory by providing its item ID.
6. **Display Inventory List**: View a list of all items in the inventory.
7. **Exit**: Close the application.

### Dependencies

This project uses the external framework `streamlit` and the Python modules `tkinter`, `bcrypt`, and `messagebox`.

**License**

No license - copyright applies.
