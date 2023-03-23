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
        for i, point in enumerate(points):
            for j in range(i + 1, len(points)):
                d = min(d, point.dist(points[j]))
        return d

    def get_strip(self, points, mid_point, distance):
        strip = []
        for point in points:
            if abs(mid_point.x - point.x) < distance:
                strip.append(point)
        return strip

    def the_min_one_compare_to_strip_min_distance(self, strip, min_distance):
        strip = sorted(strip, key=lambda p: p.y)

        base_point = strip.pop(0)
        while len(strip) > 0:
            for point in strip:
                if (point.y - base_point.y) >= min_distance:
                    break
                min_distance = min(min_distance, base_point.dist(point))
            base_point = strip.pop(0)
        return min_distance

    def min_distance(self, points):
        mid = len(points)//2
        if mid <= 1:
            return self.brute_force_min_distance(points)
        points = sorted(points, key=lambda p: p.x)

        sub_min_distance = min(self.min_distance(points[:mid]),
                               self.min_distance(points[mid:]))

        strip = self.get_strip(points, points[mid], sub_min_distance)
        return self.the_min_one_compare_to_strip_min_distance(strip, sub_min_distance)


class Converter:
    def input_to_cases(self):
        cases = []
        print("Total number of cases:")
        total_number_of_cases = int(input())
        number_of_runned_cases = 0
        while number_of_runned_cases < total_number_of_cases:
            points = []
            print("Total number of points in case %d:" % (number_of_runned_cases + 1))
            total_number_of_points = int(input())
            print("Please enter the coordinates of the 2D points:")
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
    print("Start executing...")
    cases = Converter().input_to_cases()
    for i in range(len(cases)):
        print("The closet distance of case %d is %.6f" % (i, Calculator().min_distance(cases[i])))
