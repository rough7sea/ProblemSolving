from collections import defaultdict
from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        graph = defaultdict(set)

        for left, right in edges:
            graph[left].add(right)
            graph[right].add(left)

        res = 1
        visited = [False] * n

        def dfs(i) -> int:
            visited[i] = True
            total = values[i]
            for next in graph[i]:
                if not visited[next]:
                    back_trac_sum = dfs(next)

                    if back_trac_sum % k == 0:
                        nonlocal res
                        res += 1
                    total += back_trac_sum

            return total

        dfs(0)

        return res
