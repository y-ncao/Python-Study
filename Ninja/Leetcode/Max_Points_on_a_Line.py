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
        max_points = 2
        for i in range(N-1):
            p1 = points[i]
            same = 1
            verti = 0
            slot = {}
            max_slot = 0
            for j in range(i+1, N):
                p2 = points[j]
                if p1.x == p2.x and p1.y == p2.y:
                    same += 1
                elif p1.x == p2.x:
                    verti += 1
                else:
                    k = (p1.y - p2.y)*1.0 / (p1.x - p2.x) # This 1.0 is so important
                    if k not in slot:
                        slot[k] = 0
                    slot[k] += 1
                    max_slot = max(max_slot, slot[k])
            max_points = max(max_points, same + verti, same + max_slot)
        return max_points
    # Note:
    # 1. Double loop, O(n^2)
    # 2. Need to consider same nodes, vertical nodes. final is max(cur_max, same + verti, same + slots)
    # 3. So many things need to be initialized
