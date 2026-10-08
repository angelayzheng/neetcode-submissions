class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        graph = {}

        for j in range(len(grid[0])):
            if grid[0][j] == "1":
                graph[(0, j)] = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == "1":
                    graph[(i, j)] = set()

                    # Check above
                    if i > 0:
                        if grid[i - 1][j] == "1":
                            graph[(i, j)].add((i - 1, j))
                            graph[(i - 1), j].add((i, j))

                    # Check to the left
                    if j > 0:
                        if grid[i][j - 1] == "1":
                            graph[(i, j)].add((i, j - 1))
                            graph[(i, j - 1)].add((i, j))

        seen = set()
        islands = 0

        for node in graph:
            if node not in seen:
                self.numIslandsHelper(node, graph, seen)
                islands += 1

        return islands

    def numIslandsHelper(self, node: tuple[int], graph: dict[tuple[int], set[tuple[int]]], seen: set[tuple[int]]) -> None:

        seen.add(node)

        for neighbour in graph[node]:
            if neighbour not in seen:
                self.numIslandsHelper(neighbour, graph, seen)

            