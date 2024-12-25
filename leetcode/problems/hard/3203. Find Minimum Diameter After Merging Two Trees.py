import math
from collections import defaultdict, deque
from typing import List


class Solution:
    #
    # def create_graph(self, edges):
    #     graph: dict[list] = defaultdict(list)
    #     only_one_edges = set()
    #     for left, right in edges:
    #         graph[left].append(right)
    #         graph[right].append(left)
    #
    #         if len(graph[left]) > 1:
    #             if left in only_one_edges:
    #                 only_one_edges.remove(left)
    #         else:
    #             only_one_edges.add(left)
    #
    #         if len(graph[right]) > 1:
    #             if right in only_one_edges:
    #                 only_one_edges.remove(right)
    #         else:
    #             only_one_edges.add(right)
    #     return graph, only_one_edges
    #
    # def calculate(self, dfs, edges, n) -> int:
    #     if len(edges) < 1:
    #         return 0
    #
    #     graph, only_one_edges = self.create_graph(edges)
    #     max_tree_dist = 0
    #     cache = dict()
    #     while only_one_edges:
    #         max_tree_dist = max(max_tree_dist, dfs(only_one_edges.pop(), graph, [False] * n, cache) - 1)
    #     return max_tree_dist
    #
    # def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
    #
    #     def dfs(node, graph: dict[list], visited: list, directions: dict) -> int:
    #         visited[node] = True
    #         total_dist = 0
    #         for next_node in graph[node]:
    #             if not visited[next_node]:
    #                 if (node, next_node) in directions:
    #                     next_dist = directions[(node, next_node)]
    #                 else:
    #                     next_dist = dfs(next_node, graph, visited, directions)
    #                     directions[(node, next_node)] = next_dist
    #                 total_dist = max(total_dist, next_dist)
    #         return total_dist + 1
    #
    #     max_tree_dist_1 = self.calculate(dfs, edges1, len(edges1) + 1)
    #     max_tree_dist_2 = self.calculate(dfs, edges2, len(edges2) + 1)
    #     return max(math.ceil(max_tree_dist_1 / 2) + math.ceil(max_tree_dist_2 / 2) + 1, max_tree_dist_1, max_tree_dist_2)


    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n, m = len(edges1) + 1, len(edges2) + 1

        d1 = self.get_diameter(n, edges1)
        r1 = (d1 + 1) // 2

        d2 = self.get_diameter(m, edges2)
        r2 = (d2 + 1) // 2
        return max(d1, d2, 1 + r1 + r2)

    def get_diameter(self, n: int, edges: list[list[int]]) -> int:
        if n == 1:
            return 0

        graph = [[] for _ in range(n)]

        degree = [0] * n

        for l, r in edges:
            graph[l].append(r)
            graph[r].append(l)
            degree[l] += 1
            degree[r] += 1

        leaves = deque(i for i, v in enumerate(degree) if v == 1)

        tree_size = n
        radius = 0

        while tree_size > 2:

            for _ in range(len(leaves)):
                l = leaves.popleft()
                tree_size -= 1
                degree[l] -= 1
                for r in graph[l]:
                    degree[r] -= 1
                    if degree[r] == 1:
                        leaves.append(r)
            radius += 1

        return 2 * radius + (tree_size == 2)







sol = Solution()
# print(sol.minimumDiameterAfterMerge(edges1=[[0, 1], [0, 2], [0, 3]], edges2=[[0, 1]]))
# print(sol.minimumDiameterAfterMerge(edges1=[[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
#                                     edges2=[[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]))
# print(sol.minimumDiameterAfterMerge(edges1=[[1, 0], [2, 3], [1, 4], [2, 1], [2, 5]],
#                                     edges2=[[4, 5], [2, 6], [3, 2], [4, 7], [3, 4], [0, 3], [1, 0], [1, 8]]))
# print(sol.minimumDiameterAfterMerge(edges1=[[0, 1], [2, 0], [3, 2], [3, 6], [8, 7], [4, 8], [5, 4], [3, 5], [3, 9]],
#                                     edges2=[[0, 1], [0, 2], [0, 3]]))
print(sol.minimumDiameterAfterMerge(edges1=[[3, 0], [2, 1], [2, 3]],
                                    edges2=[[0, 1], [0, 4], [3, 5], [6, 3], [7, 6], [2, 7], [0, 2], [8, 0], [8, 9]]))
