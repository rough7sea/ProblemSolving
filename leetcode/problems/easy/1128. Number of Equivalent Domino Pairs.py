from collections import defaultdict
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        m = 0
        direct = defaultdict(int)
        for a, b in dominoes:
            if direct[(a, b)] > 0:
                m += direct[(a, b)]

            direct[(a, b)] += 1
            if a != b:
                direct[(b, a)] += 1

        return m


# 1 2 3 4 5

# 3 -> 6
# 4 -> 10

sol = Solution()
# print(sol.numEquivDominoPairs(dominoes=[[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))
print(sol.numEquivDominoPairs(dominoes=[[1, 1], [2, 2], [1, 1], [1, 2], [1, 2], [1, 1]]))
