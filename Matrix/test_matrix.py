#
# Created on Mon Aug 08 2022
#
# Author: Fabian Prandl
#
# Email: fabian.prandl@student.uni-tuebingen.de
#

import unittest
import matrix
from typing import List


class TestMatrix(unittest.TestCase):
    def setUp(self):
        """SetUp in dem Testcases als Attribute der Test Klasse gesetzt werden
            Ist bei Listen besser, weil Listen in Pyhton Mutable Objects sind, falls
            ein Test eine Matrix ändert, werden die Matritzen vor jedem Test neu erstellt"""
        self.A = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        self.A_copy = [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]]
        self.B = [[15, 25, 35],
                  [36, 42, 72],
                  [55, 16, 23]]
        self.B_copy = [[15, 25, 35],
                       [36, 42, 72],
                       [55, 16, 23]]
        
        self.E = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]
        self.O = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        self.x = [[1],
                  [1],
                  [1]]
        self.y = [[1], 
                  [-1], 
                  [0]]
        
        self.x_copy = [[1],
                       [1],
                       [1]]
        self.y_copy = [[1],
                       [-1],
                       [0]]

        self.X = [[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]]
        self.Y = [[13, 45, 74, 9],
                  [54, 7, 98, 32],
                  [6, 54, 86, 12],
                  [43, 76, 1, 23]]
        self.Y_copy = [[13, 45, 74, 9],
                  [54, 7, 98, 32],
                  [6, 54, 86, 12],
                  [43, 76, 1, 23]]
        self.Z = [[1, 2, 3, 4], 
                  [5, 6, 7, 8]]

    def test_multiply(self):
        AB = [[252, 157, 248],
              [570, 406, 638],
              [888, 655, 1028]]
        AA = [[30, 36, 42],
              [66, 81, 96],
              [102, 126, 150]]
        YY = [[3430, 5580, 11745, 2652],
              [3044, 10203, 13142, 2622],
              [4026, 6204, 13144, 3090],
              [5658, 4269, 10739, 3360]]

        self.assertEqual(matrix.multiply(self.A, self.B), AB)
        self.assertEqual(matrix.multiply(self.A, self.E), self.A)
        self.assertEqual(matrix.multiply(self.A, self.A), AA)
        self.assertEqual(matrix.multiply(self.O, self.A), self.O)
        self.assertEqual(matrix.multiply(self.A, self.B), AB)
        self.assertEqual(matrix.multiply(self.X, self.Y), self.Y)
        self.assertEqual(matrix.multiply(self.Y, self.Y), YY)
        self.assertEqual(matrix.multiply(self.E, self.x), self.x)
        
    def test_addition(self):

        AB = [[16, 27, 38],
              [40, 47, 78],
              [62, 24, 32]]
        x = [[2], 
             [2], 
             [2]]

        self.assertEqual(matrix.sum(self.A, self.B), AB)
        self.assertEqual(matrix.sum(self.B, self.A), AB)
        self.assertEqual(matrix.sum(self.x, self.x), x)

    def test_only_right_dimensions_work(self):
        """Test ob Matritzen mit unterschiedlich vielen Spalten/Zeilen 
            miteinander verrechnet werden können"""
        with self.assertRaises(AssertionError):
            matrix.multiply(self.A, self.X)
            matrix.sum(self.A, self.X)

    def test_det_sarrus(self):
        """Test für die Sarrus Determinante"""
        self.assertEqual(matrix.det_sarrus(self.A), 0)
        self.assertEqual(matrix.det_sarrus(self.B), 14820)
        self.assertEqual(matrix.det_sarrus(self.E), 1)
        

    def test_det_sarrus_dimensions(self):
        """Test, dass die Funktion wirklich einen AssertionError gibt, 
            für mehr als 3x3 Matritzen"""
        with self.assertRaises(AssertionError):
            matrix.det_sarrus(self.X)

    def test_transpose(self):
        """Test für die Transponierte einer Matrix"""
        A_T = [[1, 4, 7],
               [2, 5, 8],
               [3, 6, 9]]
        B_T = [[15, 36, 55],
               [25, 42, 16],
               [35, 72, 23]]
        Y_T = [[13, 54, 6, 43],
               [45, 7, 54, 76],
               [74, 98, 86, 1],
               [9, 32, 12, 23]]
        Z_T = [[1, 5], 
               [2, 6],
               [3, 7], 
               [4, 8]]

        self.assertEqual(matrix.transpose(self.E), self.E)
        self.assertEqual(matrix.transpose(self.A), A_T)
        self.assertEqual(matrix.transpose(self.B), B_T)
        self.assertEqual(matrix.transpose(self.Y), Y_T)
        self.assertEqual(matrix.transpose(self.Z), Z_T)
        

    def test_scalar_multiplication(self):
        A = [[5, 10, 15],
             [20, 25, 30],
             [35, 40, 45]]
        
        self.assertEqual(matrix.scalar_multiplication(self.A, 5), A)
        self.assertEqual(matrix.scalar_multiplication(self.A, 0), self.O)
        
    def test_dot_product(self):
        self.assertEqual(matrix.dot_product(self.x, self.y), 0)
        self.assertEqual(matrix.dot_product(self.x, self.x), 3)
        self.assertEqual(matrix.dot_product(self.y, self.y), 2)
        self.assertEqual(matrix.dot_product(self.y, self.x), 0)
        
        
        
    def test_for_in_situ_changes(self):
        """Test, ob Änderungen auf den Objekten selber gemacht wurden, 
            oder ob neue Objekte erstellt wurden. Änderungen auf den Objekten, 
            führen zu super schwer zu findenden Bugs, deshalb besser eine Neue 
            Matrix erstellen, als die gegebene Matrix zu verändern"""
        matrix.multiply(self.A, self.B)
        self.assertEqual(self.A, self.A_copy)
        matrix.sum(self.A, self.B)
        self.assertEqual(self.A, self.A_copy)
        self.assertEqual(self.B, self.B_copy)
        matrix.det_sarrus(self.A)
        self.assertEqual(self.A, self.A_copy)
        matrix.transpose(self.A)
        self.assertEqual(self.A, self.A_copy)
        matrix.scalar_multiplication(self.A, 5)
        self.assertEqual(self.A, self.A_copy)
        matrix.dot_product(self.x, self.y)
        self.assertEqual(self.x, self.x_copy)
        self.assertEqual(self.y, self.y_copy)
        
        