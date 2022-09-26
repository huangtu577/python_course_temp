import unittest
import matrix_numpy as matrix
from typing import List
import numpy as np


class TestMatrix(unittest.TestCase):
    def setUp(self):
        """SetUp in dem Testcases als Attribute der Test Klasse gesetzt werden
            Ist bei Listen besser, weil Listen in Pyhton Mutable Objects sind, falls
            ein Test eine Matrix ändert, werden die Matritzen vor jedem Test neu erstellt"""
        self.A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
        self.A_copy = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
        self.B = np.array([[15, 25, 35],
                  [36, 42, 72],
                  [55, 16, 23]])
        self.B_copy = np.array([[15, 25, 35],
                       [36, 42, 72],
                       [55, 16, 23]])
        
        self.E = np.array([[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]])
        self.O = np.array([[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]])
        self.x = np.array([[1],
                  [1],
                  [1]])
        self.y = np.array([[1], 
                  [-1], 
                  [0]])
        
        self.x_copy = np.array([[1],
                       [1],
                       [1]])
        self.y_copy = np.array([[1],
                       [-1],
                       [0]])

        self.X = np.array([[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])
        self.Y = np.array([[13, 45, 74, 9],
                  [54, 7, 98, 32],
                  [6, 54, 86, 12],
                  [43, 76, 1, 23]])
        self.Y_copy = np.array([[13, 45, 74, 9],
                  [54, 7, 98, 32],
                  [6, 54, 86, 12],
                  [43, 76, 1, 23]])
        self.Z = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8]])
    def test_multiply(self):
        AB = np.array([[252, 157, 248],
              [570, 406, 638],
              [888, 655, 1028]])
        AA = np.array([[30, 36, 42],
              [66, 81, 96],
              [102, 126, 150]])
        YY = np.array([[3430, 5580, 11745, 2652],
              [3044, 10203, 13142, 2622],
              [4026, 6204, 13144, 3090],
              [5658, 4269, 10739, 3360]])

        self.assertTrue((matrix.multiply(self.A, self.B) == AB).all())
        self.assertTrue((matrix.multiply(self.A, self.E) == self.A).all())
        self.assertTrue((matrix.multiply(self.A, self.A) == AA).all())
        self.assertTrue((matrix.multiply(self.O, self.A) == self.O).all())
        self.assertTrue((matrix.multiply(self.A, self.B) == AB).all())
        self.assertTrue((matrix.multiply(self.X, self.Y) == self.Y).all())
        self.assertTrue((matrix.multiply(self.Y, self.Y) == YY).all())
        self.assertTrue((matrix.multiply(self.E, self.x) == self.x).all())
        
    def test_addition(self):

        AB = self.A + self.B
        x = self.x + self.x

        self.assertTrue((matrix.sum(self.A, self.B) == AB).all())
        self.assertTrue((matrix.sum(self.B, self.A)== AB).all())
        self.assertTrue((matrix.sum(self.x, self.x)== x).all())

    

    
        

    def test_det(self):
        """Test für die Determinante"""
        self.assertAlmostEqual(matrix.det(self.A), np.linalg.det(self.A))

    def test_transpose(self):
        """Test für die Transponierte einer Matrix"""
        
        self.assertTrue((matrix.transpose(self.E) == self.E.T).all())
        self.assertTrue((matrix.transpose(self.A) == self.A.T).all())
        self.assertTrue((matrix.transpose(self.B) == self.B.T).all())
        self.assertTrue((matrix.transpose(self.Y) == self.Y.T).all())
        self.assertTrue((matrix.transpose(self.Z) == self.Z.T).all())
        

    def test_scalar_multiplication(self):
        
        
        self.assertTrue((matrix.scalar_multiplication(self.A, 5) == (self.A * 5)).all())
        self.assertTrue((matrix.scalar_multiplication(self.A, 0) ==  self.O).all())
        
    def test_dot_product(self):
        self.assertEqual(matrix.dot_product(self.x.T, self.y), 0)
        self.assertEqual(matrix.dot_product(self.x.T, self.x), 3)
        self.assertEqual(matrix.dot_product(self.y.T, self.y), 2)
        self.assertEqual(matrix.dot_product(self.y.T, self.x), 0)
        
        
        
    