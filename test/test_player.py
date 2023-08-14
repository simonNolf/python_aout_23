import unittest
from player import Player

class TestPLayer(unittest.TestCase):
    def test_addpoint(self):
        p=Player()
        p.addpoints(5)
        self.assertEqual(p.getpointsplayer(), 5005)