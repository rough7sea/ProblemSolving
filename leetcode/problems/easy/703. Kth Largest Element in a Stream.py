from heapq import heappop, heappush, heapify, heappushpop
from typing import List
from bisect import bisect_left


#
class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.pq = nums[:min(k, len(nums))]
        heapify(self.pq)
        for i in range(k, len(nums)):
            heappushpop(self.pq, nums[i])

    def add(self, val):
        heappush(self.pq, val)
        if len(self.pq) > self.k:
            heappop(self.pq)
        return self.pq[0]


# class KthLargest:
#
#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         if len(nums) == 0:
#             self.nums = nums
#             self.min = None
#         else:
#             if len(nums) >= k:
#                 self.nums = sorted(nums)[len(nums) - k:]
#             else:
#                 self.nums = sorted(nums)
#             self.min = self.nums[0]
#
#     def search(self, x: int) -> int:
#         i = bisect_left(self.nums, x)
#         if i:
#             return i-1
#         else:
#             return -1
#
#     def add(self, val: int) -> int:
#         if self.min and len(self.nums) < self.k and val < self.min:
#             return self.min
#
#         i = self.search(val)
#         self.nums.insert(i + 1, val)
#         if len(self.nums) > self.k:
#             self.nums.pop(0)
#         return self.nums[0]


# [2, 4, 5, 8]

# [4, 5, 8]
# [5, 5, 8]

# dict() {5:1, 4:1, 8:1}
#  {5:2, 4:1, 8:1}


# k = 3
# nums = [4, 5, 8, 2]

# [[2,[0]],[-1],[1],[-2],[-4],[3]]

k = 2
nums = [-4, -5, -8, -2]

# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(k, nums)
print(obj.add(-1))
print(obj.add(1))
print(obj.add(-2))
print(obj.add(-4))
print(obj.add(3))
