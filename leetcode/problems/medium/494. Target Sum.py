from typing import List


class Solution:
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     res = 0
    #     n = len(nums)
    #     total = sum(nums)
    #
    #     def rec(i: int, s: int, used: int):
    #         if i == n:
    #             if s == target:
    #                 nonlocal res
    #                 res += 1
    #         else:
    #
    #             diff = total - used
    #             if diff < abs(target - s):
    #                 return
    #
    #             rec(i + 1, s + nums[i], used + nums[i])
    #             rec(i + 1, s - nums[i], used + nums[i])
    #
    #     rec(0, 0, 0)
    #     return res

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = sum(nums)
        if (total + target) % 2 != 0 or total < abs(target):
            return 0

        subtarget = (total + target) // 2

        dp = [0] * (subtarget+1)
        dp[0] = 1

        for num in nums:
            for i in range(subtarget, num-1, -1):
                dp[i] = dp[i-num] + dp[i]

        return dp[subtarget]

sol = Solution()
# print(sol.findTargetSumWays(nums=[10,12,16,24,3,38,24,35,45,20,12,18,25,24,1,26,9,18,29,28], target=31))
# print(sol.findTargetSumWays(nums=[12,25,42,49,41,15,22,34,28,31], target=35))
# print(sol.findTargetSumWays(nums=[1,25,12,19,4,15,10,14,20,11], target=21))
print(sol.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))


