from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec(temp: list, unused: list):
            if len(unused) < 1:
                res.append(temp)
                return

            for e in set(unused):
                nex_temp = temp.copy()
                next_unused = unused.copy()
                nex_temp.append(e)
                next_unused.remove(e)
                rec(nex_temp, next_unused)

        rec([], nums)
        return res

sol = Solution()
print(sol.permuteUnique(nums=[1, 1, 2, 8, 8]))