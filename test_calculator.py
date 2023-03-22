import unittest
import math
from calculator import Point, Calculator


class CalculatorTestCase:
    def __init__(self, point_list, ans):
        self.point_list = point_list
        self.ans = ans


class CalculatorTest(unittest.TestCase):
    def test_one_points_base_cases(self):
        cases = [CalculatorTestCase([Point(0, 0)], -1),
                 CalculatorTestCase([Point(0, -1)], -1)]
        for case in cases:
            self.assertEqual(len(case.point_list), 1)
            self.assertEqual(Calculator().closest_distance(case.point_list), case.ans)

    def test_two_points_base_cases(self):
        cases = [CalculatorTestCase([Point(0, 0), Point(1, 1)], math.sqrt(2)),
                 CalculatorTestCase([Point(0, -1), Point(-1, -1)], 1)]
        for case in cases:
            self.assertEqual(len(case.point_list), 2)
            self.assertEqual(Calculator().closest_distance(case.point_list), case.ans)

    def test_three_points_base_cases(self):
        cases = [CalculatorTestCase([Point(0, 0), Point(1, 1), Point(1, 3)], math.sqrt(2)),
                 CalculatorTestCase([Point(0, 0), Point(0, -1), Point(-1, -1)], 1)]
        for case in cases:
            self.assertEqual(len(case.point_list), 3)
            self.assertEqual(Calculator().closest_distance(case.point_list), case.ans)

    def test_ten_points_base_cases(self):
        cases = [CalculatorTestCase([Point(6, 13), Point(1, 11), Point(20, 6), Point(3, 3), Point(6, 19),
                                     Point(9, 2), Point(7, 10), Point(1, 1), Point(13, 8), Point(18, 8)], math.sqrt(8))]
        for case in cases:
            self.assertEqual(len(case.point_list), 10)
            self.assertEqual(Calculator().closest_distance(case.point_list), case.ans)
