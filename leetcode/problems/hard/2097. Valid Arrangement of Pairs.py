from collections import defaultdict
from typing import List


class Solution:

    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        inOutCount = defaultdict(int)

        for i, o in pairs:
            inOutCount[i] += 1
            inOutCount[o] -= 1
            graph[i].append(o)

        start = pairs[0][0]
        for node in inOutCount:
            if inOutCount[node] == 1:
                start = node
                break

        path = []

        def dfs(node):
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)
                path.append((node, next_node))

        dfs(start)
        return path[::-1]


sol = Solution()
print(sol.validArrangement(pairs=[[8, 9], [7, 8], [6, 7], [5, 6]]))
print(sol.validArrangement(pairs=[[5, 1], [4, 5], [11, 9], [9, 4]]))
print(sol.validArrangement(pairs=[[1, 2], [1, 3], [2, 1]]))

print(sol.validArrangement(pairs=[[1, 3], [3, 4], [0, 1], [1, 2], [2, 1], ]))

print(sol.validArrangement(pairs=[[8, 5], [8, 7], [0, 8], [0, 5], [7, 0], [5, 0], [0, 7], [8, 0], [7, 8]]))
