from collections import Counter
from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        c = Counter(skill)
        team_sum = min(skill) + max(skill)
        res = 0

        while len(c.keys()) > 0:
            first = list(c.keys())[0]
            second = team_sum - first
            if second not in c:
                return -1

            first_freq = c[first]
            second_freq = c[second]
            if first_freq != second_freq:
                return -1

            del c[first]
            del c[second]

            total_freq = first_freq
            if first == second:
                total_freq /= 2

            res += (first * second * int(total_freq))
        return res


sol = Solution()
print(sol.dividePlayers([3, 2, 5, 1, 3, 4]))
print(sol.dividePlayers([3, 4]))
