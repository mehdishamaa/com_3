import unittest
import pytest
from Calculator import *


calc = Calculator()

class test_calc(unittest.TestCase):

    calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(4, 5), 9)

    def test_mul(self):
        self.assertEqual(self.calc.mul(4, 4), 16)

    def test_div(self):
        self.assertEqual(self.calc.div(9, 3), 3)

    def test_sub(self):
        self.assertEqual(self.calc.sub(10, 6), 4)








