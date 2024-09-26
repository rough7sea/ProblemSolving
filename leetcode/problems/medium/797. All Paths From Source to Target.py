from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        queue = [(0, [0])]
        n = len(graph) - 1
        res = []
        while queue:
            u, visited = queue.pop()
            for f in graph[u]:
                new_visited = visited.copy()
                new_visited.append(f)
                if f == n:
                    res.append(new_visited)
                else:
                    queue.append((f, new_visited))
        return res


sol = Solution()
print(sol.allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]))
