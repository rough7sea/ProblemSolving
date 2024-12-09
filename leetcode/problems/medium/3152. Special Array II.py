from bisect import bisect_left
from typing import List


class Solution:

    # def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
    #     res = []
    #
    #     starts = []
    #     start_to_end_dict = dict()
    #     end_to_start_dict = dict()
    #     start = 0
    #     for i in range(len(nums) - 1):
    #         if nums[i] % 2 == nums[i + 1] % 2:
    #             if i - start < 1:
    #                 start = i + 1
    #                 continue
    #             starts.append(start)
    #             start_to_end_dict[start] = i
    #             end_to_start_dict[i] = start
    #             start = i + 1
    #
    #     if start != len(nums) - 1:
    #         starts.append(start)
    #         start_to_end_dict[start] = len(nums) - 1
    #         end_to_start_dict[len(nums) - 1] = start
    #
    #     for start, end in queries:
    #         if start == end:
    #             res.append(True)
    #             continue
    #         if len(starts) == 0:
    #             res.append(False)
    #             continue
    #
    #         if start in start_to_end_dict and end <= start_to_end_dict[start]:
    #             res.append(True)
    #             continue
    #
    #         if end in end_to_start_dict and start >= end_to_start_dict[end]:
    #             res.append(True)
    #             continue
    #
    #         left = bisect_left(starts, start)
    #         if left > len(starts) or (left > 0 and starts[left] > start):
    #             left -= 1
    #
    #         if start < left:
    #             res.append(False)
    #             continue
    #
    #         left_end: bool = start_to_end_dict[left] >= end
    #         res.append(left_end)
    #     return res
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        runningSum = 0
        partialSum = []
        oddEven = None

        for num in nums:
            if num % 2 == oddEven:
                runningSum += 1
            oddEven = num % 2
            partialSum.append(runningSum)

        out = []

        for start, end in queries:
            out.append(partialSum[start] == partialSum[end])
        return out


sol = Solution()
# print(sol.isArraySpecial(nums=[3, 4, 1, 2, 6], queries=[[0, 4]]))
#
# print(sol.isArraySpecial(nums=[3, 4, 1, 2, 6, 5, 8, 7, 9, 9, 0, 1, 2, 3, 4, 4], queries=[[0, 4]]))
# print(sol.isArraySpecial(nums=[4, 3, 1, 6], queries=[[0, 2], [2, 3]]))
# print(sol.isArraySpecial(nums=[1, 1], queries=[[0, 1]]))
# print(sol.isArraySpecial(nums=[3, 7, 8], queries=[[0, 2]]))
# print(sol.isArraySpecial(nums=[5, 8, 8, 9], queries=[[1, 2]]))
# print(sol.isArraySpecial(nums=[8, 10, 1, 2, 8, 9], queries=[[0, 5]]))
# print(sol.isArraySpecial(nums=[2, 2, 3, 6, 8, 7, 4, 9], queries=[[2, 3]]))
print(sol.isArraySpecial(nums=[2, 1, 4, 7, 8, 5, 6, 4, 3, 10], queries=[[2, 5]]))
