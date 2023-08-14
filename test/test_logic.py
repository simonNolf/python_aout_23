import unittest
from logic import Logic
from player import Player


class test_logic(unittest.TestCase):
    def test_point(self):
        l = Logic()
        self.assertEqual(l.Point(Player),0)