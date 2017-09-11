# -*- coding:utf-8 -*-
def add (*values):
    result = 0
    for i in values:
        result += i
    return result

def fibo (index):
    a, b = 1, 1
    for _ in range(index):
        a, b = a + b, a
    return b

def matrix (ary):
    import numpy as np
    matrix = np.array(ary)
    if round(np.linalg.det(matrix)) != 0.0:
        return np.round(np.linalg.inv(matrix), 2)
