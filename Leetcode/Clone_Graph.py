"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        # Use oldNode as the oldGraph, newNode as the newGraph. Use tuple (oldNode, newNode) to store relation
        newNodeHead = UndirectedGraphNode(node.label)
        queue = collections.deque()
        queue.append((node,newNodeHead))
        map_dict = {}
        while len(queue) > 0:
            (oldNode,newNode) = queue.popleft()
            if oldNode in map_dict:
                continue
            map_dict[oldNode] = 'Visited'
            newNode.neighbors = []
            for oldNeighbor in oldNode.neighbors:
                newNeighbor = UndirectedGraphNode(oldNeighbor.label)
                queue.append((oldNeighbor, newNeighbor))
                newNode.neighbors.append(newNeighbor)
        return newNodeHead

    # Another way to this is like Nine Chapter, no need to do like level order BFS
    # Finally add all neighbors
