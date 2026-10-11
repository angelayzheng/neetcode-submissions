class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False
        
        graph = {i: set() for i in range(n)}

        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])

        visited = set()
        if not self.dfs(0, graph, visited, -1):
            return False

        return n == len(visited)

    def dfs(self, n: int, graph: dict[int, set[int]], seen: set[int], parent: int) -> bool:
        seen.add(n)

        for neighbour in graph[n]:
            if neighbour != parent:
                if neighbour in seen or not self.dfs(neighbour, graph, seen, n):
                    return False

        return True
