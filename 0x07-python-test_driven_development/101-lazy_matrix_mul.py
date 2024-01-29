#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (list): The first matrix represented as a list of lists.
        m_b (list): The second matrix represented as a list of lists.

    Returns:
        The result of the matrix multiplication.

    """
    return (np.matmul(m_a, m_b))
