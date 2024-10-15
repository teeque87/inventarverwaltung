import random  # Import des random-Moduls

anzahl = 10  # Anzahl der zu generierenden Zufallszahlen
summe = 0  # Initialisierung der Summe
a = []  # Leere Liste zum Speichern der Zufallszahlen
i = 0  # Initialisierung des Zählers

# Generiere eine Liste von Zufallszahlen
while i < anzahl:
    zufallszahl = random.randint(1, 99)  # Zufallszahl zwischen 1 und 99 generieren
    a.append(zufallszahl)  # Zufallszahl zur Liste hinzufügen
    i += 1  # Zähler erhöhen

# Initialisiere kleinster und größter Wert mit dem ersten Element der Liste
kleinster_wert = min(a)
größter_wert = 0

i = 0  # Zähler zurücksetzen

# Durchlaufe die Liste, um die Summe zu berechnen, und finde den kleinsten und größten Wert
while i < anzahl:
    summe = sum(a)  # Setze summe auf den aktuellen Wert (dies wird immer der Wert der aktuellen Zahl sein)
    if a[i] < kleinster_wert:
            kleinster_wert = a[i]  # Aktualisiere den kleinsten Wert, wenn der aktuelle Wert kleiner ist
    if a[i] > größter_wert:
        größter_wert = a[i]  # Aktualisiere den größten Wert, wenn der aktuelle Wert größer ist
    i += 1  # Zähler erhöhen

i = 0  # Zähler zurücksetzen

# Ausgabe der Zufallszahlen
while i < anzahl:
    print(a[i], end=" ")  # Zufallszahlen ausgeben
    i += 1  # Zähler erhöhen

# Ergebnisse ausgeben
print(f"\nDie Summe der Zufallszahlen (immer letzte Zahl) ist: {summe}")
print(f"Der kleinste Wert ist: {kleinster_wert}")
print(f"Der größte Wert ist: {größter_wert}")