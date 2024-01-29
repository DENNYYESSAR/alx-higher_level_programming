#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list): The first matrix represented as a list of lists.
        m_b (list): The second matrix represented as a list of lists.

    Returns:
        list: The result of the matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list,
                   if m_a or m_b is not a list of lists,
                   if m_a or m_b is empty,
                   if one element of m_a or m_b is not an integer or a float,
                   if each row of m_a or m_b is not of the same size.
        ValueError: If m_a and m_b cannot be multiplied.

    """

    # Check if m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list" or "m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a) or \
    not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists" or
                        "m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty" or
                         "m_b can't be empty")

    # Check if m_a and m_b contain only integers or floats
    for row in m_a:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("m_b should contain only integers or floats")

    # Check if each row of m_a and m_b has the same size
    if not all(len(row) == len(m_a[0]) for row in m_a) or \
    not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size" or
                        "each row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                sum += m_a[i][k] * m_b[k][j]
            row.append(sum)
        result.append(row)

    # Return the result matrix
    return result
