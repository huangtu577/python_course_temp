# Python Programmierkurs zum selber Lernen

Dieses Repository ist für Leute gedacht, die Python Programmieren lernen wollen,
aber nicht so wirklich wissen, wo sie anfangen sollen.
Hier findet ihr ein paar Aufgaben, die euch grundlegende Konzepte in Python näher
bringen sollen und anschließend ein paar Aufgaben, die euch entweder im Physikalischen
Praktikum oder unterm Semester begegnen können. 
## Aufgaben
Meine Vorgeschlagene Reihenfolge ist:
- Setup: Hier wird erklärt, wie ihr Anaconda installiert, damit ihr starten könnt.
- Matrix: Hier lernt ihr Listen kennen, ein sehr wichtiges Konzept beim Programmieren
- Dictionaries: Hier geht es um das Arbeiten mit Dictionaries, das kann wichtig
werden, wenn ihr Daten in irgendeiner Weise speichern wollt. Außerdem ist das 
Verhalten von Dicts und Pandas.DataFrames (wir später sehr praktisch sein um Daten 
zu verarbeiten) sehr ähnlich.
- Sunspots: Hier geht es um das einlesen von Daten und um erste Auswertungen davon.
- Curve Fitting: Hier gibt es zwei Aufgaben, die ähnlich in einem Praktikumsversuch kommen könnten.
- Bar Plots: Hier geht es darum, Daten einzulesen und damit Plots zu erstellen.
- Sperical Harmonics: Hier gibt es keine Aufgabe, sondern Beispielcode, wie man die Kugelflächenfunktionen, die z.B.das Wasserstoffatom beschreiben visualisieren kann. Spiel hier ruhig mit dem Code und schau, ob du beispielsweise die Anzahl/Reihenfolge/Farbe... der Plots ändern kannst.
- Sympy: Hier gibt es Beispielcode, wie ihr Integrale/DGL/Gleichungen mit Python lösen könnt, wenn euch WolframAlpha nicht reicht.

## Lösungen
Wie die meisten Sachen, lernt man programmieren nur durch programmieren.  Es ist gut, den Code zu lesen, aber lernen tust du nur, wenn du selber den Code änderst und versuchst Bugs zu beheben. Deshalb empfehle ich dir, nicht bei den Aufgaben, an denen du hängst, dirket in die Lösung zu schauen, sondern auf StackOverflow zu schauen, ob du eine Antwort auf deine Frage findest. Ein Großteil des Programmieren besteht aus gutem Googlen. Zu allen Aufgaben gibt es Lösungen. Dein Code muss aber nicht genauso sein, wie meine Beispiellösung. Solange dein Code auf die richtigen Ergenisse kommt, ist es gut. Trotzdem empfehle ich dir, den Lösungscode anzuschauen, da dort auch Best Practices festgehalten sind. 
## Tests
Zu einigen Aufgaben habe ich Testcases geschrieben. Diese erkennst du daran, dass die Dateien *test_bsp.py* heißen. Diese kannst du, folgendermaßen laufen lassen:
- Bearbeite die Aufgaben in den dafür geschriebenen Vorlagen.
- Wenn du eine Funktion geschrieben hast, gehe in dein Terminal, sodass du in dem Ordner bist, in dem sowohl dein Code, als auch der testcode liegt. (Dazu musst du dein virtual Environment aktiviert haben)

~~~bash
(studium) fabian@PC:~/Documents/Pyhton_course/Matrix$ ls
matrix.py   test_matrix.py  Matrix-Aufgaben.md
~~~
- In diesem Verzeichnis musst du nun in deinem Terminal eingeben:
~~~bash
(studium) fabian@PC:~/Documents/Pyhton_course/Matrix$ python -m unittest.py -v
~~~
Damit wird im Akutellen Verzeichnis nach *test... .py* Dateien gesucht und diese werden laufen gelassen. 
Damit siehst du dann, ob deine Funktionen so funktionieren wie sie sollen.

## Resourcen
Solltet ihr weiter interessiert sein, verlinke ich hier ein paar YouTube Kanäle,
 die ich hilfreich finde:
- https://www.youtube.com/c/mCodingWithJamesMurphy
- https://www.youtube.com/c/TechWithTim
- https://www.youtube.com/c/Coreyms
- https://realpython.com/

Viel Spaß beim Programmieren. Wenn ihr Fehler findet, erstellt einfach ein Pull Request, damit ich den Fehler korrigieren kann.