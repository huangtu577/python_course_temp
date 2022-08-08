# Aufgaben
## Matritzen 
### a) Matrix-Matrix-Produkt
Schreibe eine Funktion "multiply", die zwei Matritzen miteinander multipliziert. Eine Matrix wird für diese Aufgabe als eine Liste von Listen abgenommen. Die Funktion soll folgende Signatur erfüllen. 
~~~python
def multiply(A: List[List[float]], 
             B: List[List[float]]) -> List[List[float]]
~~~
Die Funktion soll einen AssertionError geben, wenn die Matritzen miteinander unkompatibel sind.
Es kann angenommen werden, dass 
~~~python
M = [[1, 2, 3], 
    [4, 5, 6, 7], 
    [8, 9, 0]]
~~~
nicht vorkommt. Das heißt, dass alle Spalten der Matrix selbe Länge haben.

### b) Matrix-Matrix-Summe
Schreibe eine Funktion "sum", die zwei Matritzen miteinder addiert. Die Funktion soll wieder folgende Signatur erfüllen. 
~~~python
def sum(A: List[List[float]], 
        B: List[List[float]]) -> List[List[float]]
~~~
Außerdem soll die Funktion wieder einen AssertionError geben, wenn die Matritzen unkompatibel sind.

### c) Skalarmultiplikation einer Matrix
Schreibe die Funktion "scalar_multiplication", die eine Matrix mit einem Skalar multipliziert und die folgende Signatur erfüllt
~~~python 
def scalar_multiplication(A: List[List[float]], 
                          t: float) -> List[List[float]]
~~~
### d) Determinante mit Sarrus-Formel
Schreibe eine Funktion "det_sarrus", die die Determinante einer 3x3-Matrix berechnet, mit 
~~~python
def det_sarrus(A: List[List[float]]) -> float
~~~
Die Funktion soll einen AssertionError geben, wenn eine nicht 3x3 Matrix gegeben ist.

### e) Transponierte einer Matrix
Schreibe eine Funktion "transpose", die die Transponierte einer Matrix berechnet:
~~~python
def transpose(A: List[List[float]]) -> List[List[float]]
~~~

### f) Skalar Produkt
Schreibe eine Funktion "dot_product", die das Skalarprodukt aus zwei 1xn Matritzen bildet. 
~~~python 
def dot_product(A: List[List[float]], 
                B: List[List[float]]) -> float
~~~
Wenn die Vektoren nicht kompatibel sind, soll ein AssertionError kommen.


# Automatische Tests
Sobald die Funktionen implementiert sind, können automatisierte Tests die Korrektheit deines Codes prüfen. Dazu musst du in der Command-Line (deinem Terminal) in das Directory wechseln, in dem die *matrix.py* und die *test_matrix.py* Dateien liegen. Dann gib folgendes in dein Terminal ein:
~~~bash
$ python -m unittest -v
~~~
Unittest sucht dann in dem Aktuellen working directory nach Datein, die mit test... .py benannt sind, und lässt diese Laufen.

Das *-v* steht für verboose mode, das heißt, du bekommst mehr Information, welche von den Tests erfolgreich waren und welche Fehlgeschlagen sind. Für mehr Informationen verwende die Flag *-h* damit wird dir eine Erklärung zu den verschiedenen Optionen angezeigt.
