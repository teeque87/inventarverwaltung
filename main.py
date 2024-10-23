from view.menu import Menu
from view.InventarGui import InventarGUI
import tkinter as tk
import sys

def main():
    while True:
        try:
            print("**** Inventarverwaltung ****")
            print("1.) GUI")
            print("2.) Konsole")
            print("3.) Beenden")
            choice = int(input("\nBitte Auswahl treffen: "))
            if choice == 1:
                root = tk.Tk()
                app = InventarGUI(root)
                root.lift()
                root.attributes('-topmost',True)
                root.after_idle(root.attributes,'-topmost',False)
                root.mainloop()
            if choice == 2:
                Menu()
            if choice == 3:
                sys.exit(1)
        except ValueError:
            print("Bitte mögliche Auswahl treffen.")


if __name__ == "__main__":
    main()