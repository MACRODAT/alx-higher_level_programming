#!/usr/bin/python3
"""using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplication of 2 matrices.

    Args:
        m_a (list of lists of ints/floats): The 1 matrix.
        m_b (list of lists of ints/floats): The 2 matrix.
    """

    return (np.matmul(m_a, m_b))
