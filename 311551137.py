import math
import sys


class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def dist(self, p):
        return math.sqrt((self.x - p.x)*(self.x - p.x) + (self.y - p.y)*(self.y - p.y))


class Calculator:
    def brute_force_min_distance(self, points):
        d = sys.maxsize
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = min(d, points[i].dist(points[j]))
        return d

    def get_strip(self, points, mid_point, distance):
        strip = []
        for point in points:
            if abs(mid_point.x - point.x) < distance:
                strip.append(point)
        return strip

    def get_strip_min_distance(self, strip):
        strip_sorted_by_y = sorted(strip, key=lambda p: p.y)
        d = sys.maxsize
        while len(strip_sorted_by_y) > 0:
            end = min(8, len(strip_sorted_by_y))
            for i in range(1, end):
                d = min(d, strip_sorted_by_y[0].dist(strip_sorted_by_y[i]))
            strip_sorted_by_y.pop(0)
        return d

    def min_distance(self, points):
        mid = len(points)//2
        if mid <= 1:
            return self.brute_force_min_distance(points)
        points_sorted_by_x = sorted(points, key=lambda p: p.x)

        sub_min_distance = min(self.min_distance(points_sorted_by_x[:mid]),
                               self.min_distance(points_sorted_by_x[mid + 1:]))

        strip = self.get_strip(points, points_sorted_by_x[mid], sub_min_distance)
        strip_closest_distance = self.get_strip_min_distance(strip)

        return min(sub_min_distance, strip_closest_distance)


class Converter:
    def input_to_cases(self):
        cases = []
        # print("Total number of cases:")
        total_number_of_cases = int(input())
        number_of_runned_cases = 0
        while number_of_runned_cases < total_number_of_cases:
            points = []
            # print("Total number of points in case %d:" % (number_of_runned_cases + 1))
            total_number_of_points = int(input())
            # print("Please enter the coordinates of the 2D points:")
            numder_of_inputted_points = 0
            while numder_of_inputted_points < total_number_of_points:
                points.append(self.input_to_point(input()))
                numder_of_inputted_points += 1
            cases.append(points)
            number_of_runned_cases += 1
        return cases

    def input_to_point(self, text):
        cordinate = text.split(" ")
        return Point(cordinate[0], cordinate[1])


if __name__ == '__main__':  # pragma: no cover
    cases = Converter().input_to_cases()
    for i in range(len(cases)):
        print("%.6f" % (float(Calculator().min_distance(cases[i]))))
