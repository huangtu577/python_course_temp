# Daten einlesen mit Pandas und DataFrames
## Sunspots
In dem Datenset *sunspot_data.csv* sind Daten über Sonnenflecken von 1818 bis 2019 gespeichert. 
### Aufgabe 1
Lies die Daten mithilfe von pd.read_csv() ein.

### Aufgabe 2
Die erste Spalte des DataFrames enthält nur die Nummer der Zeile. Entferne diese Spalte

### Aufgabe 3
In der Spalte *Number of Sunspots* ist die Anzahl der Sonnenflecken angegeben. Wenn es für einen gegebenen Tag keine Beobachtung gab, steht in dieser Spalte der Wert -1.
Entferne alle Einträge aus dem Dataset, für die keine Beobachtung vorliegt.

### Aufgabe 4 
Finde die Gesamtanzahl und den Mittelwert an beobachteten Sonnenflecken, im Zeitraum 1.1.1900 - 31.12.1999.

### Aufgabe 5
Mache einen Plot, in dem die Kummulierte Summe bis zu Tag 'x' als y-Wert gegen die Nummer des Tages geplottet werden soll. Verwende auf dem Plot für die y-Achse eine
Logarithmische Skalierung.