import unittest
from points import Points

class test_point(unittest.TestCase):
    def test_winningPoint(self):
        p = Points()
        self.assertEqual(p.getwinningpoint("9"), 3)