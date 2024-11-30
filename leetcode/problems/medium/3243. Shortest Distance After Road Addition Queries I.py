from collections import defaultdict, deque
from heapq import heappop, heappush
from typing import List


class Solution:
    # def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
    #     res = []
    #     shorts = dict()
    #
    #     for query in queries:
    #         e, v = query
    #
    #         if v <= e:
    #             res.append(res[-1])
    #             continue
    #
    #         if e not in shorts:
    #             shorts[e] = []
    #         shorts[e].append(v)
    #
    #         queue = [(0, 0)]
    #         visited = [0 for i in range(n)]
    #         while queue:
    #             time, pos = heappop(queue)
    #             visited[pos] = 1
    #             if pos == n - 1:
    #                 res.append(time)
    #                 break
    #
    #             if visited[pos + 1] == 0:
    #                 heappush(queue, (time + 1, pos + 1))
    #
    #             if pos in shorts:
    #                 for s in shorts[pos]:
    #                     if visited[s] == 0:
    #                         heappush(queue, (time + 1, s))
    #
    #     return res

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i in range(n - 1):
            adj[i].append(i + 1)

        depth = [i for i in range(n)]

        def bfs(node):
            q = deque([node])
            while q:
                n = q.popleft()
                for nei in adj[n]:
                    if depth[nei] > depth[n] + 1:
                        depth[nei] = depth[n] + 1
                        q.append(nei)

        ans = []
        for s, e in queries:
            adj[s].append(e)
            adj[s].sort(reverse=True)
            if depth[e] > depth[s] + 1:
                depth[e] = depth[s] + 1
                bfs(e)
            ans.append(depth[-1])
        return ans


# n = 20
# [0,2],[2,4],[4,6],[6,8],[8,10],[10,12],[12,14],[14,16]
# [1,9]


sol = Solution()
# print(sol.shortestDistanceAfterQueries(n=5, queries=[[2, 4], [0, 2], [0, 4]]))
print(sol.shortestDistanceAfterQueries(
    n=20, queries=[[0, 2], [2, 4], [4, 6], [6, 8], [8, 10], [10, 12], [12, 14], [14, 16]]))
