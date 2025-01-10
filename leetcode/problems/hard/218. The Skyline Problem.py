from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


class Solution:
    # def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    # heights = defaultdict(list)
    # for start, end, height in buildings:
    #     heights[start].append(height)
    #     heights[end].append(-height)
    #
    # intervals = sorted(list(heights.keys()))
    # state = defaultdict(int)
    # state[0] = 1
    # res = []
    # prev = 0
    # for i in intervals:
    #     for height in sorted(heights[i]):
    #         if height > 0:
    #             state[height] += 1
    #         else:
    #             state[abs(height)] -= 1
    #             if state[abs(height)] == 0:
    #                 del state[abs(height)]
    #     m = max(state.keys())
    #     if m != prev:
    #         res.append([i, m])
    #     prev = m
    # return res
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if len(buildings) == 0:
            return []

        buildings.sort(key=lambda v: v[2])
        pos, height = [0], [0]
        for left, right, h in buildings:
            i = bisect_left(pos, left)
            j = bisect_right(pos, right)
            height[i:j] = [h, height[j - 1]]
            pos[i:j] = [left, right]
        # print(height, pos)
        res = []
        prev = 0
        for v, h in zip(pos, height):
            if h != prev:
                res.append([v, h])
                prev = h
        return res


sol = Solution()
# print(sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
# print(sol.getSkyline(buildings=[[0, 2, 3], [2, 5, 3]]))
# print(sol.getSkyline(buildings=[[0, 3, 3], [1, 5, 3], [2, 4, 3], [3, 7, 3]]))
print(sol.getSkyline(buildings=[[5, 15, 20], [10, 15, 20], [20, 25, 5]]))
