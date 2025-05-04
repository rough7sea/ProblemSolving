from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return -1
        res = 1
        cur = 1
        prev_diff = -(nums[0] - nums[1])

        for i in range(1, len(nums)):
            diff = nums[i-1] - nums[i]

            if diff >= 0 and cur == 1:
                prev_diff = diff
                continue

            if abs(diff) == 1:
                if prev_diff == -diff:
                    cur += 1
                else:
                    cur = 2
                res = max(res, cur)
                prev_diff = diff

            else:
                cur = 1
                prev_diff = 0
        return res if res > 1 else -1

sol = Solution()
# print(sol.alternatingSubarray(nums = [2,3,4,3,4]))
# print(sol.alternatingSubarray(nums = [4,5,6]))
# print(sol.alternatingSubarray(nums = [1,29,30,5]))
print(sol.alternatingSubarray(nums = [1,2,2,1,2,3,6,2]))

