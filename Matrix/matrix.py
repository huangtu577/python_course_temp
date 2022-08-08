#
# Created on Mon Aug 08 2022
#
# Author: Fabian Prandl
#
# Email: fabian.prandl@student.uni-tuebingen.de
#

from __future__ import annotations
from typing import List

def multiply(A: List[List[float]], 
             B: List[List[float]]) -> List[List[float]]:
    """Funktion, die das Matrix Produkt aus zwei Matritzen bildet

    Parameters
    ----------
    A : List[List[float]]
        Matrix
    B : List[List[float]]
        Matrix
        
    Raises
    -----
    AssertionError
        Wenn die Beiden Matritzen nicht miteinander kompatibel sind

    Returns
    -------
    List[List[float]]
        Eine neue Matrix, die das Prudkt der beiden Matritzen A, B ist
    """    
    assert len(A[0]) == len(B), "Die Matritzen sind nicht mitenander kompatibel"
    
    # Erstellt eine neue leere Matrix
    C = initialize_empty_matrix(rows = len(A))
    
    # vgl: https://de.wikipedia.org/wiki/Matrizenmultiplikation
    for i in range(len(A)):
        for k in range(len(B[0])):
            c_ik = 0
            for j in range(len(A[0])):
                c_ik += A[i][j]*B[j][k]
            C[i].append(c_ik)
            
    return C
    
            
            

def initialize_empty_matrix(rows: int) -> List[List]:
    """Helper Funktion, die eine Leere Matrix erstellt, mit gegebener Anzahl Spalten

    Parameters
    ----------
    rows : int
        Anzahl Spalten, der neuen Matrix

    Returns
    -------
    List[List]
        Leere Matrix
    """    
    A = []
    
    # Wenn man in Python den Wert einer Variable nicht verwenden wird, ist es
    # best Practice die Variable _ zu nennen
    for _ in range(rows):
        A.append([])
    return A
    

def sum(A: List[List[float]], 
        B: List[List[float]]) -> List[List[float]]:
    """Berechnet die Summe Elementweise aus zwei Matritzen

    Parameters
    ----------
    A : List[List[float]]
        Matrix
    B : List[List[float]]
        Matrix

    Raises
    ------
    AssertionError
        - Wenn die beiden Matritzen unterschiedliche Anzahl an Spalten haben
        - Wenn die beiden Matritzen unterschiedliche Anzahl an Reihen haben
    
    Returns
    -------
    List[List[float]]
        Neue Matrix, die die Summe aus den beiden Matritzen ersten Matritzen ist
    """    
    assert len(A) == len(B), "Die Matritzen sind nicht mitenander kompatibel"
    assert len(A[0]) == len(B[0]), "Die Matritzen sind nicht miteinander kompatibel"
    
    # Initalisiere eine Leere Matrix
    C = initialize_empty_matrix(len(A))
    
    
    for i in range(len(A)): 
        for j in range(len(A[0])):
            C[i].append(A[i][j] + B[i][j])
    
    return C

def det_sarrus(A: List[List[float]]) -> float:
    """Sarrus Determinante für 3x3 Matritzen

    Parameters
    ----------
    A : List[List[float]]
        Matrix

    Raises
    ------
    AssertionError
        - Wenn die Matrix nicht 3x3 ist
    Returns
    -------
    float
        Determinante
    """    
    assert len(A) == 3, "Sarrus Determinante funktioniert nur für 3x3 Matritzen"
    assert len(A[0]) == 3, "Sarrus Determinante funktioniert nur für 3x3 Matritzen"
    det = 0
    
    for i in range(3):
        # Die Zeilen, die addiert werden
        # Das Zeichen i += 1 ist eine Kurzform für i = i + 1
        det += A[(0 + i) % 3][0] * A[(1 + i) % 3][1] * A[(2 + i) % 3][2]
        
        # Die Zeilen, die subtrahiert werden
        det -= A[(0 + i)%3][2] * A[(1 + i) % 3][1] * A[(2 + i) % 3][0]

    return det

def scalar_multiplication(A: List[List[float]], 
                          t: float) -> List[List[float]]:
    """Skalarmultiplikation einer Matrix 

    Parameters
    ----------
    A : List[List[float]]
        Matrix
    t : float
        Skalarwert

    Returns
    -------
    List[List[float]]
        Neue Matrix
    """    
    
    C = initialize_empty_matrix(len(A))
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i].append(A[i][j] * t)
       
      
    return C

def transpose(A: List[List[float]]) -> List[List[float]]:
    """Berechnet die Transponierte einer Matrix.

    Parameters
    ----------
    A : List[List[float]]
        Matrix

    Returns
    -------
    List[List[float]]
        Transponierte der Matrix
    """    
    A_T = initialize_empty_matrix(len(A[0]))
    
    for i in range(len(A[0])):
        for j in range(len(A)):
            a = A[j][i]
            A_T[i].append(a)
    
    return A_T
        

def dot_product(A: List[List[float]], 
                B: List[List[float]]) -> float:
    """Skalarprodukt zwischen zwei 1xn Matritzen

    Parameters
    ----------
    A : List[List[float]]
        Vektor 1
    B : List[List[float]]
        Vektor 2

    Raises
    -------
        - AssertionError, wenn die beiden Vektoren unterschiedliche Länge haben
        - AssertionError, wenn die beiden Vektoren mehr als einen Eintrag pro
            Zeile haben
    Returns
    -------
    float
        Skalarprodukt
    """    
    
    assert len(A) == len(B), "Die Vektoren sind unterschiedlich lang"
    assert len(A[0]) == 1 & len(B[0]) == 1, "Nicht möglich für Matritzen"
    
    C = 0
    
    for i in range(len(A)):
        C += A[i][0]*B[i][0]

    return C    