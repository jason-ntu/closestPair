import unittest
import math
import calculator
from calculator import Point


class Case:
    def __init__(self, x0, y0, x1, y1, ans):
        self.points = [Point(x0, y0), Point(x1, y1)]
        self.ans = ans


class ClosestDistanceTest(unittest.TestCase):
    def testBasic(self):
        cases = [Case(0, 0, 1, 1, math.sqrt(2))]
        for case in cases:
            self.assertEqual(calculator.closestDistance(case.points), case.ans)
