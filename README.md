![enter image description here](https://tse1.mm.bing.net/th?id=OIG4.k5fL_MZmyAwPGwWDYhMZ&pid=ImgGn)


# Inventarverwaltungssystem Version mit CLI


## **Überblick**

Dieses Inventarverwaltungssystem ist eine auf Python basierende Anwendung, die dazu dient, Produkte, Produktgruppen und Lagerbestände effizient zu verwalten. 
Es bietet Funktionen zum Hinzufügen, Bearbeiten und Löschen von Artikeln und Artikelgruppen sowie zur Verwaltung von Wareneingang und -ausgang. 
Das System bietet außerdem eine Bestandswarnung bei niedrigem Lagerbestand und ermöglicht eine schnelle Artikelsuche.


## **Funktionen**

- **Artikel anlegen/bearbeiten/löschen:** Verwalte einzelne Artikel im Inventar durch Hinzufügen, Bearbeiten oder Löschen.
- **Artikelgruppen anlegen/bearbeiten/löschen:** Gruppiere Artikel in Kategorien und verwalte diese.
- **Lagerverwaltung:** Verwalte Wareneingang (Bestand erhöhen) und Warenausgang (Bestand reduzieren) problemlos.
- **Bestandswarnung:** Erhalte eine Warnung, wenn der Lagerbestand einen kritischen Schwellenwert unterschreitet.
- **Artikelsuche:** Finde Artikel schnell durch Suche nach Artikel-ID oder Produktname.
- **Inventarliste anzeigen:** Zeige alle aktuell im Bestand befindlichen Artikel an.


## Verwendete Technologien

Python: Die Programmiersprache, die für dieses Projekt verwendet wird.
SQLite: Die Datenbank die verwendet wird
ItemServices: Ein benutzerdefiniertes Modul, das die Operationen im Zusammenhang mit Artikeln und Lagerbeständen abwickelt.

Terminal-basierte Benutzeroberfläche: Die Anwendung läuft in der Konsole und interagiert über eine textbasierte Eingabe und Ausgabe mit dem Benutzer.
GUI mit Tkinter: Die Anwendung läuft auch über eine GUI und interagiert über eine Eingabefelder mit den eingebauten Operationen und zeigt ansprechend die Ausgabe über die GUI Elemente an.
  

## **Erste Schritte**  

**Voraussetzungen**

Stelle sicher, dass `Python` auf deinem System installiert ist. Überprüfe die Python-Version mit folgendem Befehl:
```
python --version
```

**Installation**

Klone das Repository:
```
git clone https://github.com/teeque87/inventarverwaltung.git
```

Wechsle in das Projektverzeichnis:
```
cd inventarverwaltungssystem
```

Abhängigkeiten installieren (vorzugsweise in einer virtuellen Umgebung (Environment wie z.b. venv, anaconda))

```
pip install tk
pip install bcrypt
pip install streamlit
```

Zum Starten der Anwendung je nach Betriebssystem eines der beiden Befehle verwenden.
```
python main.py
```
```
python3 main.py
```
Um die Webanwendung zu starten bitte den folgenden Befehl im Hauptverzeichnis anwenden
```
streamlit run Inventarverwaltung.py
```

Sobald die Anwendung gestartet ist, erscheint das Hauptmenü in deinem Terminal. Dort werden dir verschiedene Optionen angeboten, wie z.B.:

  
**Hauptmenü**

- **Artikel anlegen / bearbeiten**
    - **Untermenü: Artikelverwaltung**
        - Artikel anlegen
        - Artikel bearbeiten
        - Artikel löschen
        - Zurück zum Hauptmenü
- **Artikelgruppe anlegen / bearbeiten**
    - **Untermenü: Artikelgruppenverwaltung**
        - Artikelgruppe anlegen
        - Artikelgruppe bearbeiten
        - Artikelgruppe löschen
        -Zurück zum Hauptmenü
- **Wareneingang**
    - Sucht nach einem Artikel und ermöglicht die Eingabe der Menge, die hinzugefügt werden soll.
- **Warenausgang**
    - Sucht nach einem Artikel und ermöglicht die Eingabe der Menge, die abgezogen werden soll.
- **Inventarliste ausgeben**
    - Zeigt eine Liste aller aktuell im Lager befindlichen Artikel an.
- **Artikel suchen**
    - Untermenü: Artikelsuche
        - Nach Artikel-ID suchen
        - Nach Produktnamen suchen
- **Programm beenden**
    - Beendet das Programm.

Folge den Anweisungen auf dem Bildschirm, um die Inventarverwaltung nach Bedarf zu steuern.

  
## **Zukünftige Verbesserungen**

Reporting- und Exportfunktionen (z.B. CSV- oder PDF-Berichte) einbauen.


# Inventarverwaltungssystem Version mit Gui (tkinter)

Dieses Projekt ist ein **Inventarverwaltungssystem** mit einer grafischen Benutzeroberfläche (GUI), das auf Python und dem Tkinter-Framework basiert. Es ermöglicht die Verwaltung eines Inventars durch Hinzufügen, Bearbeiten, Löschen und Suchen von Artikeln. Es bietet auch eine Übersicht über das gesamte Inventar.

## Features

-   **Artikel hinzufügen**: Ermöglicht das Hinzufügen neuer Artikel in das Inventar.
-   **Artikel bearbeiten**: Bearbeiten Sie existierende Artikel basierend auf ihrer ID.
-   **Artikel löschen**: Löschen Sie Artikel aus dem Inventar.
-   **Artikel suchen**: Suchen Sie nach Artikeln anhand ihrer ID oder ihres Namens.
-   **Inventarliste anzeigen**: Zeigen Sie eine Liste aller Artikel im Inventar an.
-   **GUI-basierte Navigation**: Benutzerfreundliche grafische Oberfläche mit einem Hauptmenü und verschiedenen Eingabeformularen.

## Anforderungen

Um dieses Projekt auszuführen, benötigen Sie:

-   **Python 3.x**
-   **Tkinter** (über Paketmanager istallieren)
-   **bcrypt** (über Paketmanager istallieren)
-   **streamlit** 
  
### Hauptmenü

Beim Start der Anwendung wird das Hauptmenü angezeigt. Von hier aus können Sie folgende Aktionen ausführen:

1.  **Artikel nach ID suchen**: Suchen Sie nach einem Artikel anhand seiner ID und zeigen Sie die Details an.
2.  **Artikel nach Name suchen**: Suchen Sie nach einem Artikel anhand seines Namens.
3.  **Artikel hinzufügen**: Fügen Sie einen neuen Artikel in das Inventar ein, indem Sie die ID, den Namen, die Menge und die Kategorie-ID eingeben.
4.  **Artikel bearbeiten**: Bearbeiten Sie die Informationen eines existierenden Artikels, indem Sie die Artikel-ID eingeben und anschließend die Details anpassen.
5.  **Artikel löschen**: Löschen Sie einen Artikel aus dem Inventar, indem Sie dessen Artikel-ID angeben.
6.  **Inventurliste anzeigen**: Zeigen Sie eine Liste aller Artikel im Inventar an.
7.  **Beenden**: Schließen Sie die Anwendung.

### Abhängigkeiten

Dieses Projekt verwendet das externe Framework `streamlit`, außerdem die Python- Module `tkinter`, `bcrypt` und `messagebox`.

**Lizenz**

Dieses Projekt steht unter der MIT-Lizenz – siehe die LICENSE-Datei für weitere Informationen.
