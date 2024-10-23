![enter image description here](https://tse1.mm.bing.net/th?id=OIG4.k5fL_MZmyAwPGwWDYhMZ&pid=ImgGn)


## Inventarverwaltungssystem




  

**Überblick**

  

Dieses Inventarverwaltungssystem ist eine auf Python basierende Anwendung, die dazu dient, Produkte, Produktgruppen und Lagerbestände effizient zu verwalten. Es bietet Funktionen zum Hinzufügen, Bearbeiten und Löschen von Artikeln und Artikelgruppen sowie zur Verwaltung von Wareneingang und -ausgang. Das System bietet außerdem eine Bestandswarnung bei niedrigem Lagerbestand und ermöglicht eine schnelle Artikelsuche.

  

**Funktionen**

  

Artikel anlegen/bearbeiten/löschen: Verwalte einzelne Artikel im Inventar durch Hinzufügen, Bearbeiten oder Löschen.

Artikelgruppen anlegen/bearbeiten/löschen: Gruppiere Artikel in Kategorien und verwalte diese.

Lagerverwaltung: Verwalte Wareneingang (Bestand erhöhen) und Warenausgang (Bestand reduzieren) problemlos.

Bestandswarnung: Erhalte eine Warnung, wenn der Lagerbestand einen kritischen Schwellenwert unterschreitet.

Artikelsuche: Finde Artikel schnell durch Suche nach Artikel-ID oder Produktname.

Inventarliste anzeigen: Zeige alle aktuell im Bestand befindlichen Artikel an.

Verwendete Technologien

Python: Die Programmiersprache, die für dieses Projekt verwendet wird.

SQLite: Die Datenbank die verwendet wird

ItemServices: Ein benutzerdefiniertes Modul, das die Operationen im Zusammenhang mit Artikeln und Lagerbeständen abwickelt.

Terminal-basierte Benutzeroberfläche: Die Anwendung läuft in der Konsole und interagiert über eine textbasierte Eingabe und Ausgabe mit dem Benutzer.

  

**Erste Schritte**

  

Voraussetzungen

Stelle sicher, dass Python auf deinem System installiert ist. Überprüfe die Python-Version mit folgendem Befehl:

  

bash

Code kopieren

python --version

Installation

Klone das Repository:

  

bash

Code kopieren:

git clone https://github.com/dein-benutzername/inventarverwaltungssystem.git

Wechsle in das Projektverzeichnis:

  

bash

Code kopieren

cd inventarverwaltungssystem

python main.py

Anwendung benutzen

Sobald die Anwendung gestartet ist, erscheint das Hauptmenü in deinem Terminal. Dort werden dir verschiedene Optionen angeboten, wie z.B.:

  

**Hauptmenü**

Artikel anlegen / bearbeiten

  

**Untermenü: Artikelverwaltung**

Artikel anlegen

Artikel bearbeiten

Artikel löschen

Zurück zum Hauptmenü

Artikelgruppe anlegen / bearbeiten

  

**Untermenü: Artikelgruppenverwaltung**

Artikelgruppe anlegen

Artikelgruppe bearbeiten

Artikelgruppe löschen

Zurück zum Hauptmenü

  

**Wareneingang**

Sucht nach einem Artikel und ermöglicht die Eingabe der Menge, die hinzugefügt werden soll.

  

**Warenausgang**

Sucht nach einem Artikel und ermöglicht die Eingabe der Menge, die abgezogen werden soll.

  

**Inventarliste ausgeben**

Zeigt eine Liste aller aktuell im Lager befindlichen Artikel an.

  

**Artikel suchen**

Untermenü: Artikelsuche

Nach Artikel-ID suchen

Nach Produktnamen suchen

  

**Programm beenden**

Beendet das Programm.

  

Folge den Anweisungen auf dem Bildschirm, um die Inventarverwaltung nach Bedarf zu steuern.

  

  

**Zukünftige Verbesserungen**

GUI hinzufügen, um die Benutzererfahrung zu verbessern.

Eine Datenbank für die dauerhafte Speicherung integrieren.

Benutzerauthentifizierung für Multi-User-Zugriff implementieren.

Reporting- und Exportfunktionen (z.B. CSV- oder PDF-Berichte) einbauen.

  

**Lizenz**

Dieses Projekt steht unter der MIT-Lizenz – siehe die LICENSE-Datei für weitere Informationen.
