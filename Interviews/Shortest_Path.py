"""
#####With Twitter & Cyan

2D array of characters
```
1 1 1 1 1
S 1 X 1 1
1 1 1 1 1
X 1 1 E 1
1 1 1 1 X
```

S is the starting point
E is the ending point
X means you cannot traverse to that point

1. Find if there is a path from S to E
2. Find the length of shortest path from S to E given the above matrix
3. Find the shortest path from S to E given the above matrix


Restriction: Move to 8 positions
"""

def find_path(map):
    M = len(map)
    N = len(map[0])
    S = None
    for i in range(M):
        if S:
            break
        for j in range(N):
            if map[i][j] == 'S':
                S = (i, j)
                break

    queue = [ ( S, [] ) ]

    while len(queue) > 0:
        current, path = queue.pop()
        x, y = current
        if x < 0 or y < 0 or x >= M or y >= N or map[x][y] == 'X':
            continue

        path.append(current)
        if map[x][y] == 'E':
            return path        # Or len(path) for question 2

        map[x][y] = 'X'        # Mark as visited

        queue.insert(0, ((x-1, y-1), path[:]))
        queue.insert(0, ((x-1, y  ), path[:]))
        queue.insert(0, ((x-1, y+1), path[:]))
        queue.insert(0, ((x  , y-1), path[:]))
        queue.insert(0, ((x  , y+1), path[:]))
        queue.insert(0, ((x+1, y-1), path[:]))
        queue.insert(0, ((x+1, y  ), path[:]))
        queue.insert(0, ((x+1, y+1), path[:]))

    return None

map = [ ['1', '1', '1', '1', '1',],
        ['S', '1', 'X', '1', '1',],
        ['1', '1', '1', '1', '1',],
        ['X', '1', '1', 'E', '1',],
        ['1', '1', '1', '1', 'X',],
        ]

print find_path(map)

# 讨论
# 1. 无论用何种方法，最好的复杂度应该都是O(m*n)因为最坏情况都是要遍历完整个图
# 2. 但是单就最好情况来说，想讨论下有没有更好的方法，主要考虑如下：
#    因为实际已知 S 和 E 的坐标，这里用到的BFS实际是和不知道终点位置是一样的，都是BFS最先的情况就是答案
#    但我觉得方法应该是可以向着终点方向走，遇到障碍让开走，如果能够实现这种方法，肯定是最优的解法，
#    希望大家能给我点思路

# 用DFS是没有意义的，因为最后的结果是你怎么都得遍历整个图
