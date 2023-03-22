import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(p1, p2):
    return math.sqrt(math.pow(p1.x - p2.x, 2)  + math.pow(p1.y - p2.y, 2))

def closestDistance(P):
    if len(P) == 2:
        return dist(P[0], P[1])
    sorted(P, key = lambda p:p.x)

    return -1

# if n == 2 return dist(N[0], N[1])

# sort N according to x
# mid = the middle point by x in sorted N
# d = min(closestPair(left), closestPair(right))
# strip = nodes within d from mid by x
# sort strip by y
# for node in strip
#     for i = 1 to 7
#         d' = min(d', dist(node, the ith later node))

# return (d, )

if __name__ == '__main__':
    Calculator.closestDistance()
