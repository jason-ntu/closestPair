import math
import sys
import unittest
from unittest.mock import patch
from src.calculator import Point, Calculator, Converter


class CalculatorTest(unittest.TestCase):
    def test_closest_distance(self):
        cases = [[[Point(0, 0)], sys.maxsize],
                 [[Point(0, 0), Point(1, 1)], math.sqrt(2)],
                 [[Point(0, 0), Point(0, -1), Point(-1, -1)], 1],
                 [[Point(6, 13), Point(1, 11), Point(20, 6), Point(3, 3), Point(6, 19), Point(9, 2), Point(7, 10), Point(1, 1), Point(13, 8), Point(18, 8)], math.sqrt(8)],
                 [[Point(7.377359, 3.113089), Point(8.899004, 4.047913), Point(3.929112, 9.695250), Point(8.377879, 7.799725), Point(5.508218, 2.498832)], 1.785861]]
        for case in cases:
            points = case[0]
            expected_distance = case[1]
            distance = Calculator().min_distance(points)
            self.assertAlmostEqual(distance, expected_distance)


class ConverterTest(unittest.TestCase):
    def test_input_to_point(self):
        case_dict = {"1 2": Point(1, 2), "0 1.1": Point(0, 1.1)}
        for line, expected_point in case_dict.items():
            point = Converter().input_to_point(line)
            self.assertEqual(point.x, expected_point.x)
            self.assertEqual(point.y, expected_point.y)

    @patch("builtins.input", side_effect=["2", "4", "6 4", "9 2", "8 7", "3 9", "5", "7.377359 3.113089", "8.899004 4.047913", "3.929112 9.695250", "8.377879 7.799725", "5.508218 2.498832"])
    def test_input_to_cases(self, mock_input):
        expected_cases = [[Point(6, 4), Point(9, 2), Point(8, 7), Point(3, 9)],
                          [Point(7.377359, 3.113089), Point(8.899004, 4.047913), Point(3.929112, 9.695250), Point(8.377879, 7.799725), Point(5.508218, 2.498832)]]
        cases = Converter().input_to_cases()
        self.assertEqual(len(cases), len(expected_cases))
        for i in range(len(cases)):
            points = cases[i]
            expected_points = expected_cases[i]
            self.assertEqual(len(points), len(expected_points))
            for j, point in enumerate(points):
                expected_point = expected_points[j]
                self.assertEqual(point.x, expected_point.x)
                self.assertEqual(point.y, expected_point.y)
