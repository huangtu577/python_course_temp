from io import StringIO
import unittest
from unittest.mock import patch
import autokaufhaus as auto



class TestAutokaufhaus(unittest.TestCase):
    def setUp(self):
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
        self.cars = {hash("".join([str(value) for value in Car_1.values()])): Car_1,
                     hash("".join([str(value) for value in Car_2.values()])): Car_2}
        
        self.len_cars = len(self.cars.values())
        
        
        
    
    def test_show_inventory(self):
        expected = "Mercedes Coupee:\n\tBaujahr: 2009\n\tSitze: 5\n\tGelaufene Kilometer: 542.0 km\n\tPreis pro 100km: 167.67 Euro\n\tEinnahmen: 678.90 Euro\n\nBMW 3er:\n\tBaujahr: 1990\n\tSitze: 3\n\tGelaufene Kilometer: 421.0 km\n\tPreis pro 100km: 200.68 Euro\n\tEinnahmen: 500.12 Euro\n\n"
        # Hier habe ich einen anderen Output gewählt, sodass der Output von der 
        # Funktion nicht während dem Test auf dem Terminal erscheint
        with patch("sys.stdout", new = StringIO()) as _:
            self.assertEqual(auto.show_inventory(self.cars), expected)
            
    def test_add_car(self):
        Car = {"Marke": "VW",
                 "Model": "Touran",
                 "Baujahr": 2019,
                 "Anzahl Sitze": 5,
                 "Kilometer": 542,
                 "Preis pro 100km": 42.69,
                 "Einnahmen": 5000.68}
        
        
        self.assertIn(Car, auto.add_car(self.cars, Car).values())
        self.assertIs(auto.add_car(self.cars, Car), self.cars, 
                      msg="Kein Neues Objekt sollte Erstellt werden, sondern\
                          nur ein Element hinzufügen")
        
    def test_remove_car(self):
        Car_1 = {"Marke": "Mercedes",
                 "Model": "Coupee",
                 "Baujahr": 2009,
                 "Anzahl Sitze": 5,
                 "Kilometer": 542,
                 "Preis pro 100km": 167.67,
                 "Einnahmen": 678.90}
        Car_2 = {"Marke": "MerZedes",
                 "Model": "Coupee",
                 "Baujahr": 2009,
                 "Anzahl Sitze": 5,
                 "Kilometer": 542,
                 "Preis pro 100km": 167.67,
                 "Einnahmen": 678.90}
        
        len_dict = len(self.cars.values())
        
        # Test, dass das Auto Tatsächlich nichtmehr in den Values des Dicts ist
        self.assertNotIn(Car_1, auto.remove_car(self.cars, Car_1).values())
        # Test, dass wirklich ein Element entfernt wurde
        self.assertEqual(len_dict - 1, len(self.cars.values()))
        # Test, dass ein Falsches Auto tatächlich nicht entfernt werden kann
        self.assertEqual(self.cars, auto.remove_car(self.cars, Car_2))
        # Test, dass sich tatsächlich die Länge der Werte nicht ändert, wenn 
        # man versucht etwas zu entfernen, was nicht im dict war
        self.assertEqual(len_dict - 1, len(self.cars.values()))
        
    
    def test_change_car(self): 
        Car_1 = {"Marke": "Mercedes",
                 "Model": "Coupee",
                 "Baujahr": 2009,
                 "Anzahl Sitze": 5,
                 "Kilometer": 542,
                 "Preis pro 100km": 167.67,
                 "Einnahmen": 678.90}
        
        Car_1_new = {"Marke": "Nissan",
                 "Model": "Coupee",
                 "Baujahr": 2009,
                 "Anzahl Sitze": 5,
                 "Kilometer": 542,
                 "Preis pro 100km": 167.67,
                 "Einnahmen": 678.90}
        
        
        self.assertIn(Car_1_new, x := auto.change_car(self.cars, 
                                                 Car_1, 
                                                 "Marke", 
                                                 "Nissan").values())
        self.assertEqual(len(x), self.len_cars)
    
    def test_change_not_existing_car(self):
        Car_1 = {"Marke": "Toyota",
                 "Model": "Coupee",
                 "Baujahr": 2009,
                 "Anzahl Sitze": 5,
                 "Kilometer": 542,
                 "Preis pro 100km": 167.67,
                 "Einnahmen": 678.90}
        self.assertRaises(AssertionError, auto.change_car, *(self.cars, 
                                                 Car_1, 
                                                 "Marke", 
                                                 "Nissan"))
    
    
        
        
            
            
        