from typing import List

import sortedcontainers


class MyMinMaxHash:

    def __init__(self):
        self.map = sortedcontainers.SortedDict()

    def add(self, num: int):
        if num in self.map:
            self.map[num] += 1
        else:
            self.map[num] = 1

    def min(self):
        if len(self.map.keys()) < 1:
            return 0
        return self.map.keys()[0]

    def max(self):
        if len(self.map.keys()) < 1:
            return 0
        return self.map.keys()[-1]

    def remove(self, num: int):
        if num in self.map:
            if self.map[num] == 1:
                self.map.pop(num)
            else:
                self.map[num] -= 1


# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         if len(nums) < 1:
#             return 0
#
#         map = MyMinMaxHash()
#         left = 0
#         right = 0
#         res = 0
#
#         while left <= right or left == len(nums):
#             while right < len(nums):
#                 cur = nums[right]
#                 map.add(cur)
#                 right += 1
#                 if map.max() - map.min() <= limit:
#                     res = max(res, right - left)
#                 else:
#                     break
#
#             if right == len(nums):
#                 break
#
#             while map.max() - map.min() > limit and left < right:
#                 map.remove(nums[left])
#                 left += 1
#         return res


from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue = deque()  # store maximum values
        min_queue = deque()  # store minimum values

        left = 0

        for n in nums:
            # Maintain the max_queue in decreasing order of elements
            while max_queue and n > max_queue[-1]:
                max_queue.pop()
            max_queue.append(n)

            # Maintain the min_queue in increasing order of elements
            while min_queue and n < min_queue[-1]:
                min_queue.pop()
            min_queue.append(n)

            # If the absolute difference between the maximum and minimum elements
            # in the current window exceeds the limit, remove one element
            # from either or both queues and increment the left pointer
            if max_queue[0] - min_queue[0] > limit:
                if max_queue[0] == nums[left]:
                    max_queue.popleft()
                if min_queue[0] == nums[left]:
                    min_queue.popleft()
                left += 1
        return len(nums) - left


sol = Solution()
# print(sol.longestSubarray(nums=[8, 2, 4, 7], limit=4))
print(sol.longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5))
