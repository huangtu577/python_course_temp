#
# Created on Mon Aug 08 2022
#
# Author: Fabian Prandl
#
# Email: fabian.prandl@student.uni-tuebingen.de
#

from __future__ import annotations
from typing import Dict, Union

Car = dict[str: str,
           str: str,
           str: int,
           str: int,
           str: float,
           str: float,
           str: float]


def show_inventory(cars: Dict[str, Car]) -> str:
    """Gibt eine Übersicht der Autos, die im Dictionary sind. Normalerweise wäre
       es ausreichen nur auf der Console eine Ausgabe zu haben, aber für die Tests
       bietet es sich an, einen Rückgabewert zu haben.

    Parameters
    ----------
    cars : Dict[str, Car]
        Datenbank an Autos

    Returns
    -------
    str
        Der String, der auch auf dem Terminal ausgegeben wird
    """    
    s = ""
    for _, value in cars.items():
        s += f"{value['Marke']} {value['Model']}:\n"
        s += f"\tBaujahr: {value['Baujahr']}\n"
        s += f"\tSitze: {value['Anzahl Sitze']}\n"
        s += f"\tGelaufene Kilometer: {value['Kilometer']:.1f} km\n"
        s += f"\tPreis pro 100km: {value['Preis pro 100km']:.2f} Euro\n"
        s += f"\tEinnahmen: {value['Einnahmen']:.2f} Euro\n"
        s += "\n"
    print(s)
    return s


def add_car(cars: Dict[int, Car],
            car: Car) -> Dict[int, Car]:
    """Fügt ein Car zum cars-Dictionary hinzu

    Parameters
    ----------
    cars : Dict[int, Car]
        Gesamtes Dictionary mit allen Autos. Der Key ist der Hash aller Attribute
        eines Cars
    car : Car
        Dictionary, in dem alle Attribute des Car gespeichert sind

    Returns
    -------
    Dict[int, Car]
        Updated Dictionary, wenn das Auto schon vorhanden war, wird einfach das
        ursprüngliche dict zurückgegeben
    """

    # Berechne den Hash des neuen Autos
    hash_car = hash("".join([str(value) for value in car.values()]))

    # # Äquivalente Implementierung:
    # s = ""
    # for value in car.values():
    #     s += str(value)
    # hash_car = hash(s)

    # Das Auto ist schon erfasst
    if hash_car in cars.keys():
        return cars

    cars[hash_car] = car
    return cars


def remove_car(cars: Dict[int, Car],
               car: Car) -> Dict[int, Car]:
    """Entfernt ein Auto aus der Datenbank. Wenn das Auto nicht vorhanden ist, 
        wird das Dictionary einfach so zurückgegeben

    Parameters
    ----------
    cars : Dict[int, Car]
        Datenbank an Autos
    car : Car
        Auto, das entfernt werden soll

    Returns
    -------
    Dict[int, Car]
        Datenbank, aus der das Auto entfernt wurde
    """    
    if car not in cars.values():
        return cars

    # Brauchen den Hash um ein Element zu Löschen
    hash_car = hash("".join([str(value) for value in car.values()]))
    del cars[hash_car]
    return cars


def change_car(cars: Dict[int, Car],
               car: Car,
               attribute: str,
               new_value: Union[str, int]) -> Dict[int, Car]:
    """Ändert ein Attribut an einem gegebenen Auto

    Parameters
    ----------
    cars : Dict[int, Car]
        Datenbank der Autos
    car : Car
        Gegebenes Auto, das geändert werden soll
    attribute : str
        Attribut, das geändert werden soll
    new_value : Union[str, int]
        Neuer Wert, der gesetzt werden soll

    Raises
    -------
    AssertionError
        - Wenn das Auto nicht vorhanden ist in der DB
        - Wenn das Attribut nicht vorhanden ist in einem Auto
    Returns
    -------
    Dict[int, Car]
        Datenbank aus Autos
    """    
    assert car in cars.values(), "Das Auto ist nicht Vorhanden im Dictionary"
    assert attribute in car.keys(), "Das Attribut hat das Auto nicht"

    hash_car = hash("".join([str(value) for value in car.values()]))
    car = cars[hash_car]
    car[attribute] = new_value
    return cars

def most_valuable(cars: Dict[int, Car]) -> List[Car]:
    sorted_cars = sorted(cars.values(), key = lambda x: x["Preis pro 100km"], reverse = True)
    return sorted_cars


if __name__ == "__main__":
    Car_1 = {"Marke": "Mercedes",
             "Model": "Coupee",
             "Baujahr": 2009,
             "Anzahl Sitze": 5,
             "Kilometer": 542,
             "Preis pro 100km": 167.67,
             "Einnahmen": 678.90}
    Car_2 = {"Marke": "BMW",
             "Model": "3er",
             "Baujahr": 1990,
             "Anzahl Sitze": 3,
             "Kilometer": 420.998,
             "Preis pro 100km": 200.6754,
             "Einnahmen": 500.123}
    cars = {hash("".join([str(value) for value in Car_1.values()])): Car_1,
            hash("".join([str(value) for value in Car_2.values()])): Car_2}
    show_inventory(cars)
    print(most_valuable(cars))
