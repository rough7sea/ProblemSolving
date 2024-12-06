from collections import defaultdict
from heapq import heappush, heappop
from typing import List

import numpy as np


class Solution:
    def maxProbability(self,
                       n: int,
                       edges: List[List[int]],
                       succProb: List[float],
                       start: int,
                       end: int) -> float:

        graph = defaultdict(list)
        for i in range(len(edges)):
            left, right = edges[i]
            prob = succProb[i]

            prob_negative = -prob
            graph[left].append((right, prob_negative))
            graph[right].append((left, prob_negative))

        if start not in graph or end not in graph:
            return 0

        queue = [(-1, start)]
        visited = [False]*n

        while queue:
            prob_negative, edge = heappop(queue)
            prob = -prob_negative

            if edge == end:
                return prob
            visited[edge] = True

            for next_edge, next_prob_negative in graph[edge]:
                next_prob = -next_prob_negative
                if visited[next_edge]:
                    continue
                # nextNodeProb = np.exp(np.log(prob) + np.log(next_prob))
                nextNodeProb = prob * next_prob
                heappush(queue, (-nextNodeProb, next_edge))

        return 0

#
# sol = Solution()
# print(sol.maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.2], start=0, end=2))
# print(sol.maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.3], start=0, end=2))
# print(sol.maxProbability(n=3, edges=[[0, 1]], succProb=[0.5], start=0, end=2))
