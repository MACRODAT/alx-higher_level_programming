#!/usr/bin/python3
import unittest
from models.base import Base
import pep8
import os

"""
TEST RUNNER
"""


class TestBase(unittest.TestCase):
    """ test runner for base """
    def setUp(self) -> None:
        """ set up """
        return super().setUp()

    def test_pep8(self):
        """ pep 8 """
        pep = pep8.StyleGuide(quiet=True)
        p = pep.check_files(['../models/base.py'])
        self.assertEqual(p.total_errors, 1, "Pycodestyle error")
    
    def test_id(self):
        """ testing id """
        b1 = Base()
        b2 = Base(2)
        b3 = Base(-1)
        b4 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, -1)
        self.assertEqual(b4.id, 2)

if __name__ == "__main__":
    unittest.main()
