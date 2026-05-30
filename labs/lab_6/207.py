class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)

        # 0 = unvisited, 1 = in progress, 2 = done
        visited = [0] * numCourses

        def has_cycle(node):
            if visited[node] == 1:
                return True
            if visited[node] == 2:
                return False

            visited[node] = 1
            for neighbor in adj[node]:
                if has_cycle(neighbor):
                    return True
            visited[node] = 2
            return False

        return not any(has_cycle(i) for i in range(numCourses))