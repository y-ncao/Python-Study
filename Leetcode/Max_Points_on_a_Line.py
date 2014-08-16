"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""

# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        N = len(points)
        if N <= 2:
            return N
        ret = 2
        for i, p1 in enumerate(points[:-1]):
            slots = {}
            same = 0
            vertical = 1
            current_max = 0
            for j, p2 in enumerate(points[i+1:]):
                if p1.x == p2.x and p1.y == p2.y:
                    same += 1
                elif p1.x == p2.x:
                    vertical += 1
                    #print vertical
                else:
                    k = (p1.y - p2.y) * 1.0 / (p1.x - p2.x)
                    if k not in slots:
                        slots[k] = 2
                    else:
                        slots[k] += 1
            for slot in slots.keys():
                current_max = max(current_max, slots[slot] + same) # Here need to check twice
            ret = max(ret, current_max, vertical+same)             # Cuz slot might be empty
        return ret
