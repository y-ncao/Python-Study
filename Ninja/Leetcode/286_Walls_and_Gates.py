"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        gates = self.find_gates(rooms)
        print(gates)
        if not gates:
            return

        for gate in gates:
            self.BFS(gate, rooms)

    def find_gates(self, rooms):
        gates = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    gates.append((i, j))
        return gates

    def BFS(self, start, rooms):
        queue = [(start, 0)]
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            cur_pos, distance = queue.pop(0)
            if (
                cur_pos in visited or
                rooms[cur_pos[0]][cur_pos[1]] == -1
            ):
                continue
            else:
                visited.add(cur_pos)

            rooms[cur_pos[0]][cur_pos[1]] = min(distance, rooms[cur_pos[0]][cur_pos[1]])

            for d in directions:
                next_point = (cur_pos[0] + d[0], cur_pos[1] + d[1])
                if (
                    0 <= next_point[0] < len(rooms) and
                    0 <= next_point[1] < len(rooms[0]) and
                    rooms[next_point[0]][next_point[1]] > distance + 1
                ):
                    queue.append((next_point, distance + 1))
