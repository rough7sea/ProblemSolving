from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec(temp: list, unused: set):
            if len(unused) < 1:
                res.append(temp)
                return

            for e in unused:
                nex_temp = temp.copy()
                next_unused = unused.copy()
                nex_temp.append(e)
                next_unused.remove(e)
                rec(nex_temp, next_unused)

        rec([], set(nums))
        return res

sol = Solution()
print(sol.permute(nums = [1, 2, 3]))

# Input: nums = [1,2,3]
# Output: [
# [1,2,3],
# [1,3,2],
# [2,1,3],
# [2,3,1],
# [3,1,2],
# [3,2,1]
# ]
