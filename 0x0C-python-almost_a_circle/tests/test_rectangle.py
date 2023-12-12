#!/usr/bin/python3
import unittest
import pep8
import os
import sys

sys.path.append(os.path.dirname(sys.path[0]))
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), "models"))

from models.base import Base
from models.rectangle import Rectangle

"""
TEST RUNNER
"""

class TestBase(unittest.TestCase):
    """ test runner for Rectangle """
    def setUp(self) -> None:
        """ set up """
        super().setUp()

    def tearDown(self) -> None:
        sys.stdout = sys.__stdout__

    def test_pep8(self):
        """ pep 8 """
        pep = pep8.StyleGuide(quiet=True)
        p = pep.check_files(['../models/rectangle.py'])
        self.assertEqual(p.total_errors, 1, "Pycodestyle error")
    
    def test_id(self):
        """ testing id """
        b1 = Rectangle(1, 2)
        b2 = Rectangle(2, 4)
        b3 = Rectangle(1, 1, 1, 1, 111)
        b4 = Rectangle(1, 2)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 111)
        self.assertEqual(b4.id, 3)



if __name__ == "__main__":
    unittest.main()
