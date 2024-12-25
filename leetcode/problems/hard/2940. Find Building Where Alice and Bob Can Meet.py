import heapq
from typing import List


class Solution:
    # def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
    #     n = len(heights)
    #
    #     decs_stack = []
    #     calc = [-1] * n
    #
    #     for i in range(n):
    #         if not decs_stack or heights[decs_stack[-1]] >= heights[i]:
    #             decs_stack.append(i)
    #             continue
    #         while decs_stack and heights[decs_stack[-1]] < heights[i]:
    #             last = decs_stack.pop()
    #             calc[last] = i
    #         decs_stack.append(i)
    #
    #     while decs_stack:
    #         pop = decs_stack.pop()
    #         calc[pop] = pop
    #
    #     res = []
    #
    #     for x, y in queries:
    #         if x > y:
    #             x, y = y, x
    #
    #         # x - less
    #         # y - more
    #         # __x_____y__
    #
    #         if x == y or heights[x] < heights[y]:
    #             res.append(y)
    #             continue
    #
    #         if heights[calc[y]] > heights[x]:
    #             res.append(calc[y])
    #             continue
    #
    #         # heights[x] - max
    #         search_height = heights[x]
    #
    #         c_max = calc[x]
    #         if c_max >= y:
    #             res.append(c_max)
    #             continue
    #
    #         x = c_max
    #         while x < y and x != calc[x]:
    #             x = calc[x]
    #
    #         if x == calc[x] and x < y:
    #             res.append(-1)
    #             continue
    #
    #         # l, r = y, x
    #         while x >= y:
    #             if x == y:
    #                 res.append(y)
    #                 break
    #
    #             m = y + (x - y) // 2
    #
    #             calc_m = calc[m]
    #
    #             if heights[calc_m] >= search_height:
    #                 x = calc_m - 1
    #             else:
    #                 y = calc_m
    #
    #     return res

    def leftmostBuildingQueries(self, heights, queries):
        max_idx = []  # Min-heap to simulate priority queue
        results = [-1] * len(queries)
        store_queries = [[] for _ in heights]

        # Store the mappings for all queries in store_queries.
        for idx, query in enumerate(queries):
            a, b = query
            if a > b:
                a, b = b, a
            if a < b and heights[a] < heights[b]:
                results[idx] = b
            elif a == b:
                results[idx] = a
            else:
                store_queries[max(a, b)].append(
                    (max(heights[a], heights[b]), idx))

        for idx, height in enumerate(heights):

            # If the heap's smallest value is less than the current height, it is an answer to the query.
            while max_idx and max_idx[0][0] < height:
                _, q_idx = heapq.heappop(max_idx)
                results[q_idx] = idx

            # Push the queries with their maximum index as the current index into the heap.
            for element in store_queries[idx]:
                heapq.heappush(max_idx, element)

        return results


sol = Solution()
# print(sol.leftmostBuildingQueries(heights=[6, 4, 8, 5, 2, 7], queries=[[1, 0], [0, 3], [2, 4], [3, 4], [2, 2]]))
print(sol.leftmostBuildingQueries(heights=[5, 3, 8, 2, 6, 1, 4, 6], queries=[[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]]))
# print(sol.leftmostBuildingQueries(heights=[3, 4, 1, 2, 5], queries=[[0, 2], ]))
