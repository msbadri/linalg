import numpy as np
from typing import Optional

def rearrange_system_of_equations(coefficient_matrix: np.ndarray,
                                  unknown_vector: np.ndarray,
                                  constant_vector: np.ndarray
                                 ) -> tuple[np.ndarray, np.ndarray]:
    """
    Rearranges a linear system A @ x = b to a standard form, where some entries of x or b are unknown.

    Parameters:
        coefficient_matrix (np.ndarray): Coefficient matrix of shape (m, m).
        unknown_vector (np.ndarray): Solution vector with some entries as `None` (unknowns).
        constant_vector (np.ndarray): Right-hand side vector with some entries as `None`.

    Returns:
        tuple: A tuple (A, b) in the standard form that can be fed to solvers.
    """
    m = coefficient_matrix.shape[0]
    if m != coefficient_matrix.shape[1] or \
       m != unknown_vector.shape[0] or \
       m != constant_vector.shape[0]:
       raise ValueError("Dimensions do not match")

    A = np.zeros([m, m])
    b = np.zeros(m)
    i = 0
    j = 0
    for number in unknown_vector:
        if number == None:
            A[:, i] = coefficient_matrix[:, j]
            i += 1
        elif number != 0:
            b -= number * coefficient_matrix[:, j]
        j += 1
    j = 0
    for number in constant_vector:
        if number == None:
            temp = np.zeros(m)
            temp[j] = -1
            A[:, i] = temp
            i += 1
        elif number != 0:
            temp = np.zeros(m)
            temp[j] = number
            b += temp
        j += 1
    return (A, b)
