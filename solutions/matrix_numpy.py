import numpy as np

def multiply(A: np.ndarray, 
             B: np.ndarray) -> np.ndarray:
    return A@B

def sum(A: np.ndarray, 
        B: np.ndarray) -> np.ndarray:
    
    return A + B

def scalar_multiplication(A: np.ndarray,
                          t: float) -> np.ndarray:
    return t*A

def transpose(A: np.ndarray) -> np.ndarray:
    return A.T

def det(A: np.ndarray) -> float:
    return np.linalg.det(A)

def dot_product(A: np.ndarray, 
                B: np.ndarray) -> float:
    return np.dot(A, B)


if __name__ == "__main__":
    A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [8, 9, 10]])
    B = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [8, 9, 10]])

    print(dot_product(A, A))
