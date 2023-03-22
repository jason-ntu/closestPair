import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def x_between(self, x0, x1):
        return x0 <= self.x and self.x <= x1

    def dist(p0, p1):
        return math.sqrt(math.pow(p0.x - p1.x, 2) + math.pow(p0.y - p1.y, 2))

class Calculator:
    def brute_force_closest_distance(self, point_list):
        n = len(point_list)
        if n == 1:
            return -1
        d = Point.dist(point_list[0], point_list[1])
        for i in range(n):
            for j in range(i + 1, n):
                d = min(d, Point.dist(point_list[i], point_list[j]))
        return d

    def closest_distance(self, point_list):
        n = len(point_list)
        if n <= 3:
            return self.brute_force_closest_distance(point_list) 
        point_list_sorted_by_x = sorted(point_list, key = lambda p:p.x)
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
        
        sorted(strip_list, key = lambda p:p.y)
        for i in range(len(strip_list)):
            for j in range(1, 8):
                if i+j < len(strip_list):            
                    d = min(d, Point.dist(strip_list[i], strip_list[i+j]))
        return d

class Converter:
    def input_to_cases(self, input):
        points = []

        lines = input.split("\n")
        left_number_of_cases = lines[0]
        line_index = 1
    
        while left_number_of_cases > 0:
            number_of_points = lines[line_index]
            next_line_index = line_index + number_of_points + 1
            for line in lines[line_index:next_line_index]:
                points.append(self.text_to_point(line))
            line_index = next_line_index
            left_number_of_cases -= 1
        return points
    
    def text_to_point(self, text):
        cordinate = text.split(" ")
        return Point(cordinate[0], cordinate[1])


if __name__ == '__main__':
    Calculator.closest_distance()
