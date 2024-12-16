from collections import deque
from typing import List


class Solution:
    # def continuousSubarrays(self, nums: List[int]) -> int:
    #     if len(nums) < 2:
    #         return 1
    #
    #     res = 0
    #     left, right = 0, 0
    #     window = dict()
    #
    #     while right < len(nums):
    #         val = nums[right]
    #         if val not in window:
    #             window[val] = 0
    #         window[val] += 1
    #
    #         min_val = min(window.keys())
    #         max_val = max(window.keys())
    #
    #         while max_val - min_val > 2:
    #             left_val = nums[left]
    #             window[left_val] -= 1
    #             if window[left_val] == 0:
    #                 del window[left_val]
    #             left += 1
    #             min_val = min(window.keys())
    #             max_val = max(window.keys())
    #
    #         if max_val - min_val <= 2:
    #             diff = right - left + 1
    #             res += diff
    #
    #         right += 1
    #     return res

    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        left = 0
        min_deque = deque()
        max_deque = deque()

        for right in range(n):
            # Update max_deque
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)

            # Update min_deque
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)

            # Shrink window if necessary
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            # Add count of subarrays ending at right
            ans += right - left + 1

        return ans


sol = Solution()
print(sol.continuousSubarrays(nums=[5, 4, 2, 4]))
