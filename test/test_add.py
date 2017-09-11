# -*- coding:utf-8 -*-
import unittest

class TestAdd(unittest.TestCase):
    """test for add def"""
    def test_add(self):
        from src.funcs import add
        self.assertEqual(add(1,2,3), 6)

if __name__ == '__main__':
    unittest.main()
