from __future__ import annotations
from typing import Dict, Union

Car = Dict[str: str,
           str: str,
           str: int,
           str: int,
           str: float,
           str: float,
           str: float]

def show_inventory(cars: Dict[int, Car]) -> str:
    pass

def add_car(cars: Dict[int, Car]) -> Dict[int, Car]:
    pass

def remove_car(cars: Dict[int, Car], 
               car: Car) -> Dict[int, Car]:
    pass

def change_car(cars: Dict[int, Car], 
               car: Car, 
               attribute: str, 
               new_value: Union[str, int]) -> Dict[int, Car]:
    pass

def most_valuable(cars: Dict[int, Car]) -> List[Car]:
    pass