from collections import deque
from math import inf
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = -inf
        max_val = values[len(values) - 1] - 1
        for i in range(len(values) - 2, -1, -1):
            if values[i] + max_val > max_score:
                max_score = values[i] + max_val

            max_val = max(max_val - 1, values[i] - 1)
        return max_score


sol = Solution()
print(sol.maxScoreSightseeingPair(values=[8, 1, 5, 2, 6]))
