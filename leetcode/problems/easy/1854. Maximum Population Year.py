from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year = [0] * (2050 - 1950 + 1)

        for b, d in logs:
            year[b - 1950] += 1
            year[d - 1950] -= 1

        m = 0
        res = 0
        cur = 0
        for i in range(len(year)):
            cur += year[i]
            if cur > m:
                m = cur
                res = i
        return 1950 + res


sol = Solution()
print(sol.maximumPopulation(logs=[[1993, 1999], [2000, 2010]]))
