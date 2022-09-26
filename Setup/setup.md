# Setup
Wenn du Anaconda (und damit Python ) schon installiert hast, brauchst du diesen Schritt nicht mehr zu 
machen. Du kannst überprüfen, ob du Python/Anaconda installiert hast:
~~~bash
foo@bar:~$ python
Python 3.8.10 (default, Jun  4 2021, 15:09:15) 
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
~~~
bzw:
~~~bash
foo@bar:~$ conda 
usage: conda [-h] [-V] command ...

conda is a tool for managing and deploying applications, environments and packages.

Options:
...
~~~
Wenn du Anaconda/Python nicht installiert hast, solltest du eine Fehlermeldung bekommen.

## Installation
Ich würde dir empfehlen, Anaconda zu installieren, darin ist Python, sowie die meisten
Module für *Scientific Computing* schon enthalten, und ihr müsst nichtmehr alles seperat installieren.

1. Lade dir die Anaconda unter https://www.anaconda.com/products/distribution für
dein Betriebssystem herunter. Ich werde hier die Installation für Linux beschreiben.
Für Windows/Mac sollte es ähnlich gehen, schau dafür eventuell mal hier https://docs.anaconda.com/anaconda/install/windows/ (für Windows) bzw. https://docs.anaconda.com/anaconda/install/mac-os/ (für MacOS) vorbei.
2. Öffne ein Terminal (am besten in dem Verzeichnis, in dem die heruntergeladene 
Datei liegt):
~~~bash
 fabian@PC:~/Downloads/Python_course$ ls
Anaconda3-2022.05-Linux-x86_64.sh
~~~
Ich bin jetzt in dem Verzeichnis, in dem die heruntergeladene Datei liegt.

3. 
Gib diesen Befehl in dein Terminal ein.
~~~bash
# Include the bash command regardless of whether or not you are using the Bash shell
bash ~/Downloads/Anaconda3-2020.05-Linux-x86_64.sh
# Replace ~/Downloads with your actual path
# Replace the .sh file name with the name of the file you downloaded
~~~
In meinem Fall würde das so aussehen:

~~~bash 
fabian@PC:~/Downloads/Python_course$ bash Anaconda3-2022.05-Linux-x86_64.sh
~~~

4. Lies und akzeptiere die AGB
5. Im nächsten Schritt fragt dich das Installationsprogramm, wo du die Datei speichern
möchtest. Ich würde dir empfehlen, den Default Pfad zu nehmen, da bei selbst vorgeschlagenen Pfaden immer mal wieder was schief geht und die ganze Installation dann schief geht.
6. Ihr werdet gefragt ob ihr die Anaconda Distribution Initialisieren wollt:  `conda init`. Akzeptiert das mit `yes`
7. Als nächstes wird dir gesagt, dass Anaconda per Default beim Start deines PCs aktiviert wird. Ich würde das, so lassen, aber du kannst es natürlich auch jedes Mal 
manuel starten. Das ist persönlicher Geschmack.
Dein Terminal sollte jetzt so aussehen:
~~~bash
(base) fabian@PC:~$ 
~~~
Das (base) steht dafür, dass du in deinem Base Environment bist (also dass Anaconda 
aktiviert ist).

Sollte deine Installation irgendwo schiefgegangen sein, gib deine Fehlermeldung mal bei Google ein, die Hälfte von Programmierung ist gutes Googlen und Foren auf StackOverflow lesen :)

## Erstellen eines Environments
In deine Environments kannst du jetzt verschiedene Module laden. Ich würde dir empfehlen, nicht das (base)- Envioronent zu verwenden, sondern ein Environment fürs 
Studium zu machen (habe ich zumindestens so gemacht). Gib dafür
~~~bash
(base) fabian@PC:~$ conda create -n studium python=3.9 --file requirements.txt
~~~
in dein Termial ein. Hinter der Flag `-n` gibst du den Namen für dein Environment an, 
nach dem Namen spezifizierst du die Pythonversion. Ich habe dir eine `requirements.txt` Datei geschrieben, in der sind alle Module gelistet, die ich bis jetzt wirklich gebraucht habe. 
Wichtig ist, dass Du Pyhton 3.x verwendest und nicht Python 2.x. 
Wenn du den Befehl laufen lassen hast und den Download bestätigt hast, sollte 
auf deinem Terminal 
~~~bash 
#
# To activate this environment, use
#
#     $ conda activate studium
#
# To deactivate an active environment, use
#
#     $ conda deactivate
~~~
stehen.
Aktiviere nun dein Environment mit 
~~~bash
(base) fabian@PC:~$ conda activate studium
~~~
Danach sollte das (base) zu einem (studium) werden:
~~~bash
(studium) fabian@PC:~$ 
~~~

Jetzt hast du dein Environment soweit vorbereitet, dass du Angangen kannst Code 
zu schreiben. 

## IDE
Es gibt viele Verschiedene IDEs für Python, von denen viele an unterschiedlichen 
Stellen Stärken haben.
- Spyder: Eignet sich sehr gut für die Auswertung von Praktika
- PyCharm: Eher geeignet für Größere Programmierprojekte, die nicht notwendigerweise
Wissenschaftlicher Natur sein müssen
- VSCode: Kann alles so bisschen, aber nichts so richtig. Ist trotzdem für mich
die IDE der Wahl, da es dort ein sehr Gutes Autocomplete gibt.
- Jupyter Lab: Eignet sich sehr gut für schöne Darstellung von Code/Auswertungen

Für die Auswertug von den Praktika würde ich dir empfehlen, *Spyder* zu verwenden:
~~~bash
(base) fabian@PC:~$ conda activate studium
(studium) fabian@PC:~$ spyder
~~~

## Autocomplete
Für VSCode gibt ein Autocomplete, das das Code Schreiben wirklich deutlich beschleunigt. Infos dazu findet ihr unter: https://www.tabnine.com/

Dort könnt ihr euch für unterschiedliche Editoren, das Autocomplete Runterladen.
In meiner Erfahrung funktioniert das Autocomplete aber leider nur in VSCode schnell
genug, um hilfreich zu sein.
