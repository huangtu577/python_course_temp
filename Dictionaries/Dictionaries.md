# Aufgabe
In dieser Aufgabe geht es um Dictionaries. Schreibe eine Daten Verwaltungssoftware 
für ein Autohaus. Die Datenbank des Autohauses sieht folgendermaßen aus:
~~~
{
    12345: {"Marke": "Mercedes", 
        "Model": "Coupee", 
        "Baujahr": 2009,
        "Anzahl Sitze": 5, 
        "Kilometer": 542, 
        "Preis pro 100km": 167.67,
        "Einnahmen": 678.90};
    98273: {...};
    ... 
}
~~~
Wobei der Key der hash des Objekts ist, um doppelte Einträge zu verhindern

## Show Inventory()
Implementiere dazu zuerst eine Funktion, mit der ein Inventar ausgegeben 
werden kann.
~~~python 
def show_inventory(cars: Dict[int, Car]) -> str
~~~
Die Ausgabe soll dabei zuerst im Scope der Funktion zu einem String zusammen 
gebastelt werden und am Ende geprintet werden (Mach dich nicht verrückt, wenn der
Test nicht Klappt, solange die Ausgabe in der Nähe von dem geforderten ist, 
sind Einrückungen vorest egal).
Hierbei steht die Abkürzung *Car* für 
~~~python 
Car = Dict[str: str,        # Marke
           str: str,        # Model
           str: int,        # Baujahr
           str: int,        # Anzahl Sitze
           str: float,      # Kilometer
           str: float,      # Preis pro 100km
           str: float       # Einnahmen
           ]
~~~
Eine Beispielausgabe ist
~~~
BMW 3er:
    Baujahr: 2009
    Sitze: 5
    Gelaufene Kilometer: 10983.7 km
    Preis pro 100km: 420.69 Euro
    Einnahmen: 69.70 Euro

Fiat Multipla: 
    Baujahr: ...
~~~
Die Ausgabe soll also der folgenden Form sein:
~~~
$Marke$ $Model$:
    Baujahr: $Baujahr$
    Sitze: $Anzahl Sitze$
    Gelaufene Kilometer: $Kilometer$ km
    Preis pro 100km: $Preis pro 100km$ Euro
    Einnahmen: $Einnahmen$ Euro

$Marke$ $Model$:
    Baujahr: $Baujahr$
    ...
~~~

## Add Car()
Schreibe eine Funktion, die zu einem Dictionary einen neuen Eintrag hinzufügt. Dabei soll der *Key* des neuen Eintrags der hash des *Car* sein.
~~~python 
add_car(cars: Dict[int, Car],
        new_car: Car) -> Dict[int, Car]
~~~
Wenn das Auto schon in dem Dictionary ist, soll es nicht nochmal eingefügt werden, 
sondern einfach das Dictionary zurückgegeben werden.

## Remove_car()
Schreibe eine Funktion, die aus dem Dictionary einen Bestehenden Eintrag löscht. Sollte das Auto nicht vorhanden sein, 
wird einfach das unveränderte Dict zurückgegeben:
~~~python 
def remove_car(cars: Dict[int, Car], 
               car: Car) -> Dict[int, Car]
~~~

## Change_Car()
Schreibe eine Funktion, die ein Bestehenden Eintrag in einem Attribut ändert. Dazu wird das Auto gegeben, und das Attribut, das geändert werden soll. Wenn
das Auto nicht vorhanden ist, soll ein AssertionError erscheinen:
~~~python 
def change_car(cars: Dict[int, Car], 
               car: Car, 
               attribute: str, 
               new_value: Union[str, int]) -> Dict[int, Car]
~~~


## most_valuable()
Schreibe eine Funktion, die eine Liste an Autos nach Wertigkeit (also der Preis pro 100km) geordnet ausgibt
(also das Teuerste zuerst).
~~~python 
def most_valuable(cars: Dict[int, Car]) -> List[Car]
~~~
dabei kann es hilfreich sein, built-In Funktionen von Python zu verwenden.

## total_earnings()
Schreibe eine Funktion, die die Gesamteinnahmen von allen Autos kalkuliert:
~~~python 
def total_earnings(cars: Dict[int, Car]) -> float
~~~
Auch hier kann es sinnvoll sein, built-In Methoden zu verwenden.


