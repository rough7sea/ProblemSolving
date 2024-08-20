from typing import List


class Solution:

    def maxDistance(self, arrays: List[List[int]]) -> int:
        if len(arrays) < 2:
            return 0
        prev_max = arrays[0][-1]
        prev_min = arrays[0][0]
        res = -1

        for arr in arrays[1:]:
            min_v = arr[0]
            max_v = arr[-1]

            res = max(max(max_v - prev_min, prev_max - min_v), res)
            prev_max = max(prev_max, max_v)
            prev_min = min(prev_min, min_v)
        return res



# [1, 5, 6][-5, 3, 6][-11, -12]
# [-15, -3][5, 15][6, 15]
# [5, 15][6, 15][-1, 0, 4]

sol = Solution()
# print(sol.maxDistance(arrays=[[1, 4], [0, 5]]))
print(sol.maxDistance(arrays=[[-1, 1], [-3, 1, 4], [-2, -1, 0, 2]]))
