from typing import List


class Solution:
    # def jump(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     if n < 2:
    #         return 0
    #     dp = [0] * n
    #     max_dict_queue = [0]
    #     for i in range(n):
    #         max_dict = max_dict_queue[0]
    #         if nums[i] < 1:
    #             while max_dict_queue[0] <= i:
    #                 max_dict_queue.pop(0)
    #             continue
    #
    #         if i + nums[i] >= n - 1:
    #             return dp[max_dict] + 1
    #
    #         if i + nums[i] > max_dict_queue[-1]:
    #             dp[i + nums[i]] = dp[max_dict] + 1
    #             while max_dict_queue[-1] > i + nums[i]:
    #                 max_dict_queue.pop()
    #             max_dict_queue.append(i + nums[i])
    #         elif dp[i + nums[i]] == 0:
    #             dp[i + nums[i]] = nums[max_dict]
    #
    #         while max_dict_queue[0] <= i:
    #             max_dict_queue.pop(0)
    #
    #     return dp[-1]
    def jump(self, nums: List[int]) -> int:
        start, reach, jumps = 0, 0, 0
        for i in range(len(nums) - 1):
            if reach < nums[i] + i:
                reach = nums[i] + i
            if i == start:
                start = reach
                jumps += 1
        return jumps


sol = Solution()
# print(sol.jump(nums=[2, 3, 1, 1, 4]))
# print(sol.jump(nums=[1, 2]))
# print(sol.jump(nums=[1, 2, 1, 1, 1]))
print(sol.jump(nums=[7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]))
# print(sol.jump(nums=[2, 0, 8, 0, 3, 4, 7, 5, 6, 1, 0, 0, 5, 9, 7, 5, 3, 6]))
