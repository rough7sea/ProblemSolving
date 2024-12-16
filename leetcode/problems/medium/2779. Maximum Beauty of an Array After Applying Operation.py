from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:

        # def max_possible(goal) -> int:
        #     count = 0
        #     for e in nums:
        #         if abs(goal - e) <= k:
        #             count += 1
        #     return count
        #
        # left = min(nums)
        # right = max(nums)
        #
        # res_max = max_possible(left)
        # res_max = max(res_max, max_possible(right))
        #
        # while left < right:
        #     m = left + (right - left) // 2
        #
        #     cur_max = max_possible(m)
        #
        #     if cur_max >

        nums.sort()

        left, right = 0, 0
        res_max = 1

        while right < len(nums):
            # A[j] - A[i] ≤ 2 * k.
            if nums[right] - nums[left] <= 2 * k:
                right += 1
                res_max = max(res_max, right - left)
            else:
                left += 1

        return res_max


sol = Solution()
print(sol.maximumBeauty(nums=[4, 6, 1, 2], k=2))
