class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        # Build graph
        graph = {}

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == 1:
                    graph[(i, j)] = set()

                    if i > 0 and grid[i - 1][j] == 1:
                        graph[(i, j)].add((i - 1, j))
                        graph[(i - 1, j)].add((i, j))

                    if j > 0 and grid[i][j - 1] == 1:
                        graph[(i, j)].add((i, j - 1))
                        graph[(i, j - 1)].add((i, j))

        # Check islands
        visited = set()

        for n in graph:
            if n not in visited:
                max_area = max(max_area, self.dfs(n, graph, visited))
                
        return max_area

    def dfs(self, n: tuple[int], graph: dict[tuple[int], set[tuple[int]]], visited: set[tuple[int]]) -> int:
        area = 1
        visited.add(n)

        for u in graph[n]:
            if u not in visited:
                area += self.dfs(u, graph, visited)
                
        return area

