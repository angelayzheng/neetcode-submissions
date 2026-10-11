"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        graph = {node.val: Node(node.val, None)}
        self.cloneGraphHelper(node, graph, set())

        return graph[node.val]

    def cloneGraphHelper(self, node: Node, graph: dict[int, Node], visited: set[int]) -> None:
        for u in node.neighbors:
            if u.val not in graph:
                graph[u.val] = Node(u.val, None)
            
            graph[node.val].neighbors.append(graph[u.val])

        visited.add(node.val)

        for u in node.neighbors:
            if u.val not in visited:
                self.cloneGraphHelper(u, graph, visited)
