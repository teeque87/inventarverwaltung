
import tkinter as tk
from tkinter import messagebox # Modul stellt Dialogboxen für verschiedene Meldungen zur Verfügung (z.B. in confirm_delete oder als Exception Anzeige)
from services.item_services import ItemServices


class InventarGUI:
    def __init__(self, root):
        """
        Initialisiert die GUI der Inventarverwaltung.

        :param root: Das Hauptfenster der Tkinter-Anwendung.
        """
        self.root = root
        self.root.title("Inventarverwaltung")
        #self.root.geometry
        self.item_services = ItemServices() # Verbindung zu ItemServices (Controller)
        root.config(bg="#2B2B2B")
        self.create_main_menu()  # Hauptmenü

        window_width = 700
        window_height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        position_x = int((screen_width - window_width) / 2)     # um die Mitte des Bildschirms zu finden
        position_y = int((screen_height - window_height) / 2)
        self.root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")      # Fenster mit Position und Größe einstellen


    def create_main_menu(self):
        """
        Erstellt das Hauptmenü der Anwendung und fügt alle Menüoptionen hinzu.
        """
        self.clear_frame()

        frame = tk.Frame(self.root, bg="#2B2B2B")
        frame.pack(pady=20) #padding y-axis, vertikales padding, def. Abstand zwischen den widgets

        label = tk.Label(frame, text="Inventarverwaltung\n - Hauptmenü -", bg="#2B2B2B", fg= "#B00E87", font=('Helvetica', 26, 'bold'))
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
            tk.Label(frame, text=text, bg="#2B2B2B", fg="white").grid(row=i+2, column=0, sticky="w", padx=10)
            btn_select = tk.Button(frame, text="Wählen", bg="#2B2B2B", fg="white", command=command)
            btn_select.grid(row=i+2, column=1, pady=5)


    def search_by_id(self):
        """
        Zeigt ein Eingabefeld zur Suche von Artikeln nach ID an.
        """
        self.clear_frame()
        frame = tk.Frame(self.root, bg="#2B2B2B")
        frame.pack(pady=100)

        label = tk.Label(frame, text="Artikel nach ID suchen", bg="#2B2B2B", fg= "#B00E87", font=("Helvetica", 14))
        label.grid(row=0, column=0, columnspan=2)

        tk.Label(frame, text="Artikel-ID: ", bg="#2B2B2B", fg="white").grid(row=1, column=0)
        entry_id = tk.Entry(frame)
        entry_id.grid(row=1, column=1)

        btn_search = tk.Button(frame, text="Suchen", bg="#2B2B2B", fg="white", command=lambda: self.handle_search_by_id((int(entry_id.get()))))
        btn_search.grid(row=2, column=0, columnspan=2, pady=10)

        btn_back = tk.Button(frame, text="Zurück", bg="#2B2B2B", fg="white", command=self.create_main_menu)
        btn_back.grid(row=3, column=0, columnspan=2, pady=5)

    def handle_search_by_id(self, product_id):
        """
        Handhabt die Suche eines Artikels anhand der gegebenen ID und zeigt den Artikel an.

        :param product_id: Die ID des zu suchenden Artikels.
        """
        try:
            all_items = self.item_services.search_items_id(product_id)
            for item in all_items:
                # print(item)
                self.display_item(item)
        except Exception as e:
            messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten: {e}")

    def display_item(self, item):
        """
        Zeigt die Informationen eines gefundenen Artikels in einer Dialogbox an.

        :param item: Der gefundene Artikel.
        """
        if item:
            messagebox.showinfo("Artikel gefunden", f"ID: {item.product_id}, Name: {item.name}, Menge: {item.amount}, Kategorie: {item.category}")
        else:
            messagebox.showwarning("Nicht gefunden", "Kein Artikel mit dieser ID gefunden.")

    def search_by_name(self):
        """
        Zeigt ein Eingabefeld zur Suche von Artikeln anhand ihres Namens an.
        """
        self.clear_frame()
        frame = tk.Frame(self.root, bg="#2B2B2B")
        frame.pack(pady=100)

        btn_search = tk.Button(frame, text="Suchen", bg="#2B2B2B", fg="white", command=lambda: self.display_item(self.item_services.search_items_name(entry_id.get())))
        btn_search.grid(row=2, column=0, columnspan=2, pady=10)

        btn_back = tk.Button(frame, text="Zurück", bg="#2B2B2B", fg="white", command=self.create_main_menu)
        btn_back.grid(row=3, column=0, columnspan=2, pady=5)

        label = tk.Label(frame, text="Artikel nach Namen suchen", bg="#2B2B2B", fg="#B00E87", font=("Helvetica", 14))
        label.grid(row=0, column=0, columnspan=2)

        tk.Label(frame, text="Artikel-Name: ", bg="#2B2B2B", fg="white").grid(row=1, column=0)
        entry_id = tk.Entry(frame)
        entry_id.grid(row=1, column=1)


    def add_item(self):
        """
        Zeigt ein Eingabefeld zur Hinzufügung eines neuen Artikels an.
        """
        self.clear_frame()
        frame = tk.Frame(self.root, bg="#2B2B2B")
        frame.pack(pady=80)

        label = tk.Label(frame, text="Neuen Artikel hinzufügen", bg="#2B2B2B", fg="#B00E87", font=("Helvetica", 14))
        label.grid(row=0, column=0, columnspan=2)

        tk.Label(frame, text="Artikel ID: ",bg="#2B2B2B", fg="white" ).grid(row=1, column=0)
        entry_id = tk.Entry(frame)
        entry_id.grid(row=1, column=1)

        tk.Label(frame, text="Artikelname: ", bg="#2B2B2B", fg="white").grid(row=2, column=0)
        entry_name = tk.Entry(frame)
        entry_name.grid(row=2, column=1)

        tk.Label(frame, text="Menge: ", bg="#2B2B2B", fg="white").grid(row=3, column=0)
        entry_amount = tk.Entry(frame)
        entry_amount.grid(row=3, column=1)

        tk.Label(frame, text="Kategorie-ID: ", bg="#2B2B2B", fg="white").grid(row=4, column=0)
        entry_category = tk.Entry(frame)
        entry_category.grid(row=4, column=1)

        btn_add = tk.Button(frame, text="Hinzufügen", bg="#2B2B2B", fg="white", command=lambda: self.item_services.add_new_item(int(entry_id.get()), entry_name.get(), int(entry_amount.get()), int(entry_category.get())))
        btn_add.grid(row=5, column=0, columnspan=2, pady=10)

        btn_back = tk.Button(frame, text="Zurück", bg="#2B2B2B", fg="white", command=self.create_main_menu)
        btn_back.grid(row=6, column=0, columnspan=2, pady=5)

    def add_article_to_db(self, name, amount, category):
        """
        Fügt einen neuen Artikel zur Datenbank hinzu und zeigt Status in Messagebox an.

        :param name: Der Name des neuen Artikels.
        :param amount: Die Menge des neuen Artikels.
        :param category: Die Kategorie-ID des neuen Artikels.
        """
        if self.item_services.add_new_item(name, amount, category):
            messagebox.showinfo("Erfolg", "Artikel erfolgreich hinzugefügt.")
        else:
            messagebox.showerror("Fehler", "Fehler beim Hinzufügen des Artikels.")

    def edit_article_by_id(self):
        """
        Zeigt ein Eingabefeld zur Bearbeitung eines Artikels anhand seiner ID an.
        """
        self.clear_frame()
        frame = tk.Frame(self.root, bg="#2B2B2B")
        frame.pack(pady=80)

        label = tk.Label(frame, text="Artikel nach ID suchen", bg="#2B2B2B", fg="#B00E87", font=("Helvetica", 14))
        label.grid(row=0, column=0, columnspan=2)

        tk.Label(frame, text="Artikel-ID: ", bg="#2B2B2B", fg="white").grid(row=1, column=0)
        entry_id = tk.Entry(frame)
        entry_id.grid(row=1, column=1)

        btn_search = tk.Button(frame, text="Suchen", bg="#2B2B2B", fg="white", command=lambda: self.handle_edit_by_id((int(entry_id.get()))))
        btn_search.grid(row=2, column=0, columnspan=2, pady=10)

        btn_back = tk.Button(frame, text="Zurück", bg="#2B2B2B", fg="white", command=self.create_main_menu)
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
        frame = tk.Frame(self.root, bg="#2B2B2B")
        frame.pack(pady=80)

        label = tk.Label(frame, text="Artikel ändern", bg="#2B2B2B", fg="#B00E87", font=("Helvetica", 14))
        label.grid(row=0, column=0, columnspan=2)

        tk.Label(frame, text="Artikel ID: ", bg="#2B2B2B", fg="white").grid(row=1, column=0)
        entry_id = tk.StringVar()
        entry_id.set(str(self.item.product_id))
        entry_id = tk.Entry(frame, textvariable=entry_id)
        #entry_id.insert(str(self.item.product_id))
        entry_id.grid(row=1, column=1)

        tk.Label(frame, text="Artikelname: ", bg="#2B2B2B", fg="white").grid(row=2, column=0)
        entry_name = tk.Entry(frame)
        entry_name.grid(row=2, column=1)

        tk.Label(frame, text="Menge: ", bg="#2B2B2B", fg="white").grid(row=3, column=0)
        entry_amount = tk.Entry(frame)
        entry_amount.grid(row=3, column=1)

        tk.Label(frame, text="Kategorie-ID: ", bg="#2B2B2B", fg="white").grid(row=4, column=0)
        entry_category = tk.Entry(frame)
        entry_category.grid(row=4, column=1)

        btn_add = tk.Button(frame, text="Hinzufügen",bg="#2B2B2B", fg="white", command=lambda: self.item_services.add_new_item(int(entry_id.get()), entry_name.get(), int(entry_amount.get()), int(entry_category.get())))
        btn_add.grid(row=5, column=0, columnspan=2, pady=10)

        btn_back = tk.Button(frame, text="Zurück", bg="#2B2B2B", fg="white", command=self.create_main_menu)
        btn_back.grid(row=6, column=0, columnspan=2, pady=5)


    def delete_article(self):
        """
        Zeigt ein Eingabefeld zur Löschung eines Artikels anhand seiner ID an.
        """
        self.clear_frame()

        frame = tk.Frame(self.root, bg="#2B2B2B")
        frame.pack(pady=100)

        label = tk.Label(frame, text="Artikel löschen", bg="#2B2B2B", fg="#B00E87", font=("Helvetica", 14))
        label.grid(row=0, column=0, columnspan=2)

        tk.Label(frame, text="Artikel-ID: ", bg="#2B2B2B", fg="white").grid(row=1, column=0)
        entry_id = tk.Entry(frame)
        entry_id.grid(row=1, column=1)

        btn_delete = tk.Button(frame, text="Löschen", bg="#2B2B2B", fg="white", command=lambda: self.confirm_delete(int(entry_id.get())))
        btn_delete.grid(row=2, column=0, columnspan=2, pady=10)

        btn_back = tk.Button(frame, text="Zurück", bg="#2B2B2B", fg="white", command=self.create_main_menu)
        btn_back.grid(row=3, column=0, columnspan=2, pady=5)

    def confirm_delete(self, product_id): # fragt Benutzer nach Bestätigung für das Löschen ine einem extra Fenster
        """
        Bestätigt die Löschung eines Artikels und führt die Löschaktion aus.

        :param product_id: Die ID des zu löschenden Artikels.
        """
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
        """
        Zeigt eine Liste aller Artikel im Inventar in einer Dialogbox an.
        """
        self.clear_frame()

        frame = tk.Frame(self.root, bg="#2B2B2B")
        frame.pack(pady=20)

        label = tk.Label(frame, text="Inventarliste", bg="#2B2B2B", fg="#B00E87", font=("Helvetica", 26))
        label.pack(pady=10)

        inventory_list = self.item_services.get_all_items()
        text_area = tk.Text(frame, wrap="word", height=15, width=60)
        text_area.pack(pady=10)

        btn_back = tk.Button(frame, text="Zurück", bg="#2B2B2B", fg="white", command=self.create_main_menu)
        btn_back.pack(pady=5)
        frame.pack()

        for item in inventory_list:
            print(item)
            text_area.insert(tk.END, f"ID: {item.product_id}, Name: {item.name}, Menge: {item.amount}, Kategorie: {item.category}\n")
        text_area.config(state=tk.DISABLED)
        text_area.pack()


    def quit_program(self):
        """
        beendet das Programm nach Messagebox-Abfrage askyesno.
        """
        #self.root.quit()
        if messagebox.askyesno("Programm beenden?",
                               "sind Sie sicher?"):
            self.root.destroy()

    def clear_frame(self):
        """
        Löscht den aktuellen Frame und setzt das Layout zurück.
        """
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
   root = tk.Tk()
   app = InventarGUI(root)
   root.mainloop()

# bei ItemServices muss in Zeile 139 bei delete_item noch der return mit True gesetzt werden, sonst gibt es einen Fehler