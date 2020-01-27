"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        for index, e in enumerate(equations):
            g_value = values[index]
            d_value = (e[1], g_value)
            d_key = e[0]
            graph.setdefault(d_key, []).append(d_value)

            if g_value != 0:
                d_value = (e[0], 1.0 / g_value)
                d_key = e[1]
                graph.setdefault(d_key, []).append(d_value)

        result = []
        for q in queries:
            result.append(self.dfs(q, graph))

        return result

    def dfs(self, query, graph):
        start = query[0]
        end = query[1]
        if start == end and start not in graph:
            return -1.0
        stack = [(start, 1)]
        visited = set(start)
        while stack:
            current, value = stack.pop()
            visited.add(current)
            if current == end:
                return value

            if current not in graph:
                continue

            edges = graph[current]
            for edge, cost in edges:
                if edge not in visited:
                    stack.append((edge, value * cost))

        return -1.0

