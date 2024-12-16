from collections import Counter
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        res = 0
        el_to_i = dict()
        for i in range(len(nums)):
            el = nums[i]
            if el not in el_to_i:
                el_to_i[el] = list()
            el_to_i[el].append(i)

        sorted_nums = sorted(set(nums))
        visited = [False] * len(nums)

        for e in sorted_nums:
            while len(el_to_i[e]) > 0:
                i = el_to_i[e].pop(0)
                if visited[i]:
                    continue

                res += e
                visited[i] = True
                if i > 0:
                    # left = nums[i - 1]
                    visited[i - 1] = True
                    # if len(el_to_i[left]) > 0 and i - 1 in el_to_i[left]:
                    #     el_to_i[left].remove(i - 1)

                if i < len(nums) - 1:
                    # right = nums[i + 1]
                    visited[i + 1] = True
                    # if len(el_to_i[right]) > 0 and i + 1 in el_to_i[right]:
                    #     el_to_i[right].remove(i + 1)
        return res


sol = Solution()
# [2,1,3,4,5,2]
# print(sol.findScore(nums=[2, 3, 5, 1, 3, 2]))
print(sol.findScore(nums=[1, 1, 1, 1, 1, 1]))
print(sol.findScore(nums=[9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(sol.findScore(nums=[2]))
print(sol.findScore(nums=[10, 44, 10, 8, 48, 30, 17, 38, 41, 27, 16, 33, 45, 45, 34, 30, 22, 3, 42, 42]))
print(sol.findScore(nums=[2, 5, 6, 6, 10]))
#
#
# [2]
# [10,44,10,8,48,30,17,38,41,27,16,33,45,45,34,30,22,3,42,42]
# [2,5,6,6,10]

# print(sol.findScore(nums=[2, 1, 3, 4, 5, 2]))
# print(sol.findScore(nums=[10, 44, 10, 8, 48, 30, 17, 38, 41, 27, 16, 33, 45, 45, 34, 30, 22, 3, 42, 42]))
# print(sol.findScore(
#     nums=[730, 1721, 1993, 1532, 962, 519, 1365, 1307, 1992, 1623, 1579, 1735, 1015, 1579, 1003, 1277, 1255, 1254, 810,
#           1767, 206, 1837, 920, 1203, 1876, 521, 625, 483, 572, 922, 1936, 1014, 1835, 694, 19, 209, 1438, 127, 1716,
#           1272, 444, 1739, 148, 1580, 802, 1093, 1543, 452, 257, 103, 877, 749, 1418, 348, 1555, 1552, 818, 555, 1628,
#           547, 553, 1742, 1062, 1199, 1987, 818, 491, 1211]))
