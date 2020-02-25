"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    islands += 1
                    self.DFS((i, j), grid, visited)

        return islands

    def DFS(self, current, grid, visited):
        directions = [(0,1), (1,0), (0, -1), (-1, 0)]

        x, y = current
        if visited[x][y]:
            return

        visited[x][y] = True
        for d in directions:
            next_x = x + d[0]
            next_y = y + d[1]

            if (
                0 <= next_x < len(grid) and
                0 <= next_y < len(grid[0]) and
                grid[next_x][next_y] == "1"
            ):
                self.DFS((next_x, next_y), grid, visited)
