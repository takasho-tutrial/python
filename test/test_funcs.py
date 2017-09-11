# -*- coding:utf-8 -*-
import unittest

class TestAdd(unittest.TestCase):
    """test for add def"""
    def test_add (self):
        from src.funcs import add
        self.assertEqual(add(1,2,3), 6)

    def test_fibo (self):
        from src.funcs import fibo
        self.assertEqual(fibo(10), 89)

    def test_matrix (self):
        import numpy as np
        from src.funcs import matrix
        assert(
            matrix([[1,2],[1,4]]),
            [[1, -2],
            [-0.5, 0.5]]
        )

if __name__ == '__main__':
    unittest.main()
