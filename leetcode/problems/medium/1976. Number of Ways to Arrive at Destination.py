import sys
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        times = [sys.maxsize] * n
        times[0] = 0
        ways = [0] * n
        ways[0] = 1

        pq = [(0, 0)]  # shortest time, node

        while pq:
            old_t, u = heappop(pq)

            for v, t in graph[u]:
                new_t = old_t + t
                if new_t < times[v]:
                    heappush(pq, (new_t, v))
                    times[v] = new_t
                    ways[v] = ways[u]
                elif new_t == times[v]:
                    ways[v] += ways[u]
        mod = 10**9+7
        return ways[-1] % mod


sol = Solution()
path = sol.countPaths(
    n=7,
    roads=[
        [0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]])
print(path)

# path = sol.countPaths(n=2, roads=[[1, 0, 10]])
#
# print(path)

