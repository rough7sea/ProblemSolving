from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i = 0
        words = set()
        res = 0
        sum = 0
        for _ in range(k):
            sum += nums[i]
            words.add(nums[i])
            i += 1

        if len(words) == k:
            res = sum

        while i < len(nums):
            sum -= nums[i - k]
            if nums[i - k] in words:
                words.remove(nums[i - k])
            sum += nums[i]
            words.add(nums[i])
            if len(words) == k:
                res = max(res, sum)
            i += 1

        return res


sol = Solution()
# print(sol.maximumSubarraySum(nums=[2, 2, 3], k=3))
# print(sol.maximumSubarraySum(nums=[1, 2, 3], k=3))
print(sol.maximumSubarraySum(nums=[9, 9, 9, 1, 2, 3], k=3))
