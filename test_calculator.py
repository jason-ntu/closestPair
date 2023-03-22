import unittest
import math
from calculator import Point, Calculator, Converter


class CalculatorTestCase:
    def __init__(self, point_list, ans):
        self.point_list = point_list
        self.ans = ans


class CalculatorTest(unittest.TestCase):
    def test_closest_distance(self):
        case_list = [[[Point(0, 0)], -1],
                     [[Point(0, 0), Point(1, 1)], math.sqrt(2)],
                     [[Point(0, 0), Point(0, -1), Point(-1, -1)], 1],
                     [[Point(6, 13), Point(1, 11), Point(20, 6), Point(3, 3), Point(6, 19), Point(9, 2), Point(7, 10), Point(1, 1), Point(13, 8), Point(18, 8)], math.sqrt(8)],
                     [[Point(7.377359, 3.113089), Point(8.899004, 4.047913), Point(3.929112, 9.695250), Point(8.377879, 7.799725), Point(5.508218, 2.498832)], 1.785861]]
        for case in case_list:
            point_list = case[0]
            expected_distance = case[1]
            distance = Calculator().closest_distance(point_list)
            self.assertAlmostEqual(distance, expected_distance)


class ConverterTestt(unittest.TestCase):
    def test_line_to_point(self):
        case_dict = {"1 2": Point(1, 2), "0 1.1": Point(0, 1.1)}
        for line, expected_point in case_dict.items():
            point = Converter().line_to_point(line)
            self.assertEqual(point.x, expected_point.x)
            self.assertEqual(point.y, expected_point.y)

    def test_lines_to_cases(self):
        case_dict = {"1\n2\n0 0\n0 1": [[Point(0, 0), Point(0, 1)]],
                     "2\n4\n6 4\n9 2\n8 7\n3 9\n5\n7.377359 3.113089\n8.899004 4.047913\n3.929112 9.695250\n8.377879 7.799725\n5.508218 2.498832":
                     [[Point(6, 4), Point(9, 2), Point(8, 7), Point(3, 9)],
                      [Point(7.377359, 3.113089), Point(8.899004, 4.047913), Point(3.929112, 9.695250), Point(8.377879, 7.799725), Point(5.508218, 2.498832)]]}
        for lines, expected_cases in case_dict.items():
            cases = Converter().lines_to_cases(lines)
            self.assertEqual(len(cases), len(expected_cases))
            for i in range(len(cases)):
                point_list = cases[i]
                expected_point_list = expected_cases[i]
                self.assertEqual(len(point_list), len(expected_point_list))
                for j in range(len(point_list)):
                    point = point_list[j]
                    expected_point = expected_point_list[j]
                    self.assertEqual(point.x, expected_point.x)
                    self.assertEqual(point.y, expected_point.y)
