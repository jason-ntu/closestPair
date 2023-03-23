import math


class Point:
    def __init__(self, x=None, y=None):
        if x is not None:
            self.x = float(x)
        if y is not None:
            self.y = float(y)

    def x_between(self, x0, x1):
        return x0 <= self.x and self.x <= x1

    def dist(self, p0, p1):
        return math.sqrt(math.pow(p0.x - p1.x, 2) + math.pow(p0.y - p1.y, 2))


class Calculator:
    def __init__(self):
        return

    def brute_force_closest_distance(self, point_list):
        n = len(point_list)
        if n == 1:
            return -1
        d = Point().dist(point_list[0], point_list[1])
        for i in range(n):
            for j in range(i + 1, n):
                d = min(d, Point().dist(point_list[i], point_list[j]))
        return d

    def closest_distance(self, point_list):
        n = len(point_list)
        if n <= 3:
            return self.brute_force_closest_distance(point_list)
        point_list_sorted_by_x = sorted(point_list, key=lambda p: p.x)
        mid_x = point_list_sorted_by_x[n//2].x

        left_point_list = point_list_sorted_by_x[:n//2]
        right_point_list = point_list_sorted_by_x[n//2 + 1:]
        d = self.closest_distance(left_point_list)
        if len(right_point_list) > 1:
            d = min(d, self.closest_distance(right_point_list))

        strip_list = []
        for point in point_list:
            if point.x_between(mid_x - d, mid_x + d):
                strip_list.append(point)

        sorted(strip_list, key=lambda p: p.y)
        for i in range(len(strip_list)):
            for j in range(1, 8):
                if i+j < len(strip_list):
                    d = min(d, Point().dist(strip_list[i], strip_list[i+j]))
        return d


class Converter:
    def __init__(self):
        return

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
        print("The closet distance of case %d is %f" % (i, Calculator().closest_distance(cases[i])))
