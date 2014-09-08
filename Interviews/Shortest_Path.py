"""
#####With Twitter
"""

M= len(map)
N = len(map[0])
visited = {}
# Maybe still not the best result
def findPath(map, current_point, end_point, length, visited):
    if current_point == end_point:
        return length
    if current_point in visited:
        return INT_MAX
    if map[current_point] == 'x':
        return INT_MAX
    visited[current_point] = True
    x, y = current_point
    return min( findPath(map, (x+1,y  ), end_point, length+ 1, visited),
                findPath(map, (x-1,y  ), end_point, length+ 1, visited),
                findPath(map, (x  ,y-1), end_point, length+ 1, visited),
                findPath(map, (x  ,y+1), end_point, length+ 1, visited) )
