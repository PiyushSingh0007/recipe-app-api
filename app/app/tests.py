"""
Sample Test
"""

from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    " Test the Calc module "
    def test_add_numbers(self):
        " Test adding two numbers "
        res = calc.add(10, 5)
        self.assertEqual(res, 15)

    def test_sub_numbers(self):
        " Test subtracting two numbers "
        res = calc.sub(5, 10)
        self.assertEqual(res, -5)


    