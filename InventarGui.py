import tkinter
import tkinter as tk
from tkinter import messagebox # Modul stellt Dialogboxen für verschiedene Meldungen zur Verfügung (z.B. in confirm_delete oder als Exception Anzeige)
from services.item_services import ItemServices


class InventarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventarverwaltung")
        self.root.geometry("400x400") # wenn vom default abgewichen werden soll, Größeneingabe
        self.item_services = ItemServices() # Verbindung zu ItemServices (Controller)
        self.create_main_menu() # Hauptmenü

    def create_main_menu(self):
        self.clear_frame()

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        label = tk.Label(frame, text="Inventarverwaltung\nHauptmenü", fg= "#B00E87", font=('Helvetica', 16, 'bold'))
        label.grid(row=0, column=0, columnspan=2)

        options = [
            ("Artikel nach ID suchen", self.search_by_id),
            ("Artikel nach Name suchen", self.search_by_name),
            ("Artikel hinzufügen", self.add_item),
            ("Artikel bearbeiten", self.edit_article_by_id),
            ("Artikel löschen", self.delete_article),
            ("Inventurliste anzeigen", self.display_inventory_list),
            ("Beenden", self.quit_program)
        ]

        for i, (text, command) in enumerate(options): # enumerate erzeugt Index i als auch jeweils Tupel-Paar in Liste (text, command)
            tk.Label(frame, text=text).grid(row=i+2, column=0, sticky="w", padx=10)
            btn_select = tk.Button(frame, text="Wählen", command=command)
            btn_select.grid(row=i+2, column=1, pady=5)

    def search_by_name(self):
        self.clear_frame()
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        btn_search = tk.Button(frame, text="Suchen", command=lambda: self.display_item(self.item_services.search_items_name(entry_id.get())))
        btn_search.grid(row=2, column=0, columnspan=2, pady=10)

        btn_back = tk.Button(frame, text="Zurück", command=self.create_main_menu)
        btn_back.grid(row=3, column=0, columnspan=2, pady=5)

        label = tk.Label(frame, text="Artikel nach Namen suchen", font=("Helvetica", 14))
        label.grid(row=0, column=0, columnspan=2)

        tk.Label(frame, text="Artikel-Name: ").grid(row=1, column=0)
        entry_id = tk.Entry(frame)
        entry_id.grid(row=1, column=1)


    def search_by_id(self):
        self.clear_frame()
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        label = tk.Label(frame, text="Artikel nach ID suchen", font=("Helvetica", 14))
        label.grid(row=0, column=0, columnspan=2)

        tk.Label(frame, text="Artikel-ID: ").grid(row=1, column=0)
        entry_id = tk.Entry(frame)
        entry_id.grid(row=1, column=1)

        btn_search = tk.Button(frame, text="Suchen", command=lambda: self.handle_search_by_id((int(entry_id.get()))))
        btn_search.grid(row=2, column=0, columnspan=2, pady=10)

        btn_back = tk.Button(frame, text="Zurück", command=self.create_main_menu)
        btn_back.grid(row=3, column=0, columnspan=2, pady=5)

    def handle_search_by_id(self, product_id):
        try:
            all_items = self.item_services.search_items_id(product_id)
            for item in all_items:
                # print(item)
                self.display_item(item)
        except Exception as e:
            messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten: {e}")

    def display_item(self, item):
        if item:
            messagebox.showinfo("Artikel gefunden", f"ID: {item.product_id}, Name: {item.name}, Menge: {item.amount}, Kategorie: {item.category}")
        else:
            messagebox.showwarning("Nicht gefunden", "Kein Artikel mit dieser ID gefunden.")

    def add_item(self):
        self.clear_frame()
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        label = tk.Label(frame, text="Neuen Artikel hinzufügen", font=("Helvetica", 14))
        label.grid(row=0, column=0, columnspan=2)

        tk.Label(frame, text="Artikel ID: ").grid(row=1, column=0)
        entry_id = tk.Entry(frame)
        entry_id.grid(row=1, column=1)

        tk.Label(frame, text="Artikelname: ").grid(row=2, column=0)
        entry_name = tk.Entry(frame)
        entry_name.grid(row=2, column=1)

        tk.Label(frame, text="Menge: ").grid(row=3, column=0)
        entry_amount = tk.Entry(frame)
        entry_amount.grid(row=3, column=1)

        tk.Label(frame, text="Kategorie-ID: ").grid(row=4, column=0)
        entry_category = tk.Entry(frame)
        entry_category.grid(row=4, column=1)

        btn_add = tk.Button(frame, text="Hinzufügen", command=lambda: self.item_services.add_new_item(int(entry_id.get()), entry_name.get(), int(entry_amount.get()), int(entry_category.get())))
        btn_add.grid(row=5, column=0, columnspan=2, pady=10)

        btn_back = tk.Button(frame, text="Zurück", command=self.create_main_menu)
        btn_back.grid(row=6, column=0, columnspan=2, pady=5)

    def add_article_to_db(self, name, amount, category):
        if self.item_services.add_new_item(name, amount, category):
            messagebox.showinfo("Erfolg", "Artikel erfolgreich hinzugefügt.")
        else:
            messagebox.showerror("Fehler", "Fehler beim Hinzufügen des Artikels.")

    def edit_article_by_id(self):
        self.clear_frame()
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        label = tk.Label(frame, text="Artikel nach ID suchen", font=("Helvetica", 14))
        label.grid(row=0, column=0, columnspan=2)

        tk.Label(frame, text="Artikel-ID: ").grid(row=1, column=0)
        entry_id = tk.Entry(frame)
        entry_id.grid(row=1, column=1)

        btn_search = tk.Button(frame, text="Suchen", command=lambda: self.handle_edit_by_id((int(entry_id.get()))))
        btn_search.grid(row=2, column=0, columnspan=2, pady=10)

        btn_back = tk.Button(frame, text="Zurück", command=self.create_main_menu)
        btn_back.grid(row=3, column=0, columnspan=2, pady=5)

        #try:
            #if amount < 0:
                #raise ValueError("Die Menge muss größer oder gleich 0 sein.")

            #self.item_services.add_new_item((product_id, name, amount, cat_id))
            #return True  # Rückgabe, um den Erfolg zu kennzeichnen
       # except Exception as e:
            #print(f"Fehler beim Aktualisieren des Artikels: {e}")
           # return False  # Rückgabe bei Fehlern

    def handle_edit_by_id(self, product_id):
        try:
            all_items = self.item_services.search_items_id(product_id)
            for item in all_items:
                print(item)
                self.edit_item(item)
        except Exception as e:
            messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten: {e}")

    def edit_item(self, item):
        self.clear_frame()
        self.item = item
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        label = tk.Label(frame, text="Artikel ändern", font=("Helvetica", 14))
        label.grid(row=0, column=0, columnspan=2)

        tk.Label(frame, text="Artikel ID: ").grid(row=1, column=0)
        entry_id = tk.StringVar()
        entry_id.set(str(self.item.product_id))
        entry_id = tk.Entry(frame, textvariable=entry_id)
        #entry_id.insert(str(self.item.product_id))
        entry_id.grid(row=1, column=1)

        tk.Label(frame, text="Artikelname: ").grid(row=2, column=0)
        entry_name = tk.Entry(frame)
        entry_name.grid(row=2, column=1)

        tk.Label(frame, text="Menge: ").grid(row=3, column=0)
        entry_amount = tk.Entry(frame)
        entry_amount.grid(row=3, column=1)

        tk.Label(frame, text="Kategorie-ID: ").grid(row=4, column=0)
        entry_category = tk.Entry(frame)
        entry_category.grid(row=4, column=1)

        btn_add = tk.Button(frame, text="Hinzufügen",
                            command=lambda: self.item_services.add_new_item(int(entry_id.get()), entry_name.get(), int(entry_amount.get()), int(entry_category.get())))
        btn_add.grid(row=5, column=0, columnspan=2, pady=10)

        btn_back = tk.Button(frame, text="Zurück", command=self.create_main_menu)
        btn_back.grid(row=6, column=0, columnspan=2, pady=5)


    def delete_article(self):
        self.clear_frame()

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        label = tk.Label(frame, text="Artikel löschen", font=("Helvetica", 14))
        label.grid(row=0, column=0, columnspan=2)

        tk.Label(frame, text="Artikel-ID: ").grid(row=1, column=0)
        entry_id = tk.Entry(frame)
        entry_id.grid(row=1, column=1)

        btn_delete = tk.Button(frame, text="Löschen", command=lambda: self.confirm_delete(int(entry_id.get())))
        btn_delete.grid(row=2, column=0, columnspan=2, pady=10)

        btn_back = tk.Button(frame, text="Zurück", command=self.create_main_menu)
        btn_back.grid(row=3, column=0, columnspan=2, pady=5)

    def confirm_delete(self, product_id): # fragt Benutzer nach Bestätigung für das Löschen ine einem extra Fenster

        if messagebox.askyesno("Bestätigung", "Möchten Sie diesen Artikel wirklich löschen?"): # askyesno-Methode gibt ja=true und nein=false zurück
            try:
                product_id = int(product_id)
                if self.item_services.delete_item(product_id):
                    messagebox.showinfo("Erfolg", "Artikel erfolgreich gelöscht.")
                else:
                    messagebox.showerror("Fehler", "Fehler beim Löschen des Artikels.")
            except ValueError:
                messagebox.showerror("Eingabefehler", "Bitte geben Sie eine gültige Artikel-ID ein.")
            except Exception as e:
                messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten: {e}")

    def display_inventory_list(self):
        self.clear_frame()

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        label = tk.Label(frame, text="Inventarliste", font=("Helvetica", 14))
        label.pack(pady=10)

        inventory_list = self.item_services.get_all_items()
        text_area = tk.Text(frame, wrap="word", height=15, width=60)
        text_area.pack(pady=10)

        for item in inventory_list:
            print(item)
            text_area.insert(tk.END, f"ID: {item.product_id}, Name: {item.name}, Menge: {item.amount}, Kategorie: {item.category}\n")
        text_area.config(state=tk.DISABLED)
        text_area.pack()

        btn_back = tk.Button(frame, text="Zurück", command=self.create_main_menu)
        btn_back.pack(pady=5)
        frame.pack()

    def quit_program(self):
        self.root.quit()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def quit_program(self):
        self.root.quit()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
   root = tk.Tk()
   app = InventarGUI(root)
   root.mainloop()

# bei ItemServices muss in Zeile 139 bei delete_item noch der return mit True gesetzt werden, sonst gibt es einen Fehler