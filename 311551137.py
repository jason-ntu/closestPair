import sys
import math

class Point:
    def __init__(self, x = None, y = None):
        if x is not None:
            self.x = float(x)
        if y is not None:
            self.y = float(y)

    def x_between(self, x0, x1):
        return x0 <= self.x and self.x <= x1

    def dist(self, p0, p1):
        return math.sqrt(math.pow(p0.x - p1.x, 2) + math.pow(p0.y - p1.y, 2))
    

def brute_force_closest_distance(point_list):
    n = len(point_list)
    if n == 1:
        return -1
    d = Point().dist(point_list[0], point_list[1])
    for i in range(n):
        for j in range(i + 1, n):
            d = min(d, Point().dist(point_list[i], point_list[j]))
    return d

def closest_distance(point_list):
    n = len(point_list)
    if n <= 3:
        return brute_force_closest_distance(point_list) 
    point_list_sorted_by_x = sorted(point_list, key = lambda p:p.x)
    mid_x = point_list_sorted_by_x[n//2].x

    left_point_list = point_list_sorted_by_x[:n//2]
    right_point_list = point_list_sorted_by_x[n//2 + 1:]
    d = closest_distance(left_point_list)
    if len(right_point_list) > 1:
        d = min(d, closest_distance(right_point_list))

    strip_list = []
    for point in point_list:
        if point.x_between(mid_x - d, mid_x + d):
            strip_list.append(point)
    
    sorted(strip_list, key = lambda p:p.y)
    for i in range(len(strip_list)):
        for j in range(1, 8):
            if i+j < len(strip_list):            
                d = min(d, Point().dist(strip_list[i], strip_list[i+j]))
    return d

def lines_to_cases(input):
    cases = []

    lines = input.split("\n")
    left_number_of_cases = int(lines[0])
    line_index = 1

    while left_number_of_cases > 0:
        points = []
        number_of_points = int(lines[line_index])
        next_line_index = line_index + number_of_points + 1
        for line in lines[line_index+1 : next_line_index]:
            points.append(line_to_point(line))
        cases.append(points)
        line_index = next_line_index
        left_number_of_cases -= 1
    return cases

def line_to_point(text):
    cordinate = text.split(" ")
    return Point(cordinate[0], cordinate[1])

def main():
    lines = sys.stdin
    cases = lines_to_cases(lines)
    for case in cases:
        print(closest_distance(case))

if __name__ == '__main__':
    main()