#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elmsments of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rws of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(rw, list) for rw in matrix) or
            not all((isinstance(elms, int) or isinstance(elms, float))
                    for elms in [num for rw in matrix for num in rw])):
        raise TypeError("Matrix must be a list of lists "
                        "integers/floats")

    if not all(len(rw) == len(matrix[0]) for rw in matrix):
        raise TypeError("All rows in the matrix must have the same length.")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("Divisor must be an integer or a floating-point number.")

    if div == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return ([list(map(lambda x: round(x / div, 2), rw)) for rw in matrix])
