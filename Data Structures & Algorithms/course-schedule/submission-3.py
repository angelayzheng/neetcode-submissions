class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # visiting tracks nodes currently in the recursion stack (backtracking)
        visiting = set()
        # visited tracks nodes confirmed to have no cycles (memoization)
        visited = set()

        def has_cycle(course: int) -> bool:
            if course in visiting:
                return True
            if course in visited:
                return False

            visiting.add(course)

            for prereq in graph[course]:
                if has_cycle(prereq):
                    return True

            visiting.remove(course)
            visited.add(course)
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False

        return True