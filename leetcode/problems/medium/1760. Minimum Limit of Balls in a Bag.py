import math
from bisect import bisect_left
from typing import List


class Solution:
    # def minimumSize(self, nums: List[int], maxOperations: int) -> int:
    #     n = len(nums)
    #     total_sum = sum(nums)
    #     min_reachable = math.ceil(total_sum / (n + maxOperations))
    #     for i in range(n - 1, -1, -1):
    #         if nums[i] <= min_reachable:
    #             total_sum -= nums[i]
    #             del nums[i]
    #
    #     nums.sort()
    #     # bin search
    #     max_reachable = nums[-1]
    #     min_reachable = math.ceil(total_sum / (len(nums) + maxOperations))
    #
    #     def find_min_bin(min_possible, max_operations, array) -> int:
    #         while array:
    #             el = array.pop()
    #             cost = math.ceil(el / min_possible) - 1
    #             max_operations -= cost
    #             if max_operations < 0:
    #                 break
    #         return max_operations
    #
    #     if find_min_bin(min_reachable, maxOperations, nums.copy()) == 0:
    #         return min_reachable
    #
    #     while find_min_bin(max_reachable, maxOperations, nums.copy()) < 0:
    #         max_reachable *= 2
    #
    #     while min_reachable != max_reachable:
    #
    #         med = min_reachable + (max_reachable - min_reachable) // 2
    #         med_value = find_min_bin(med, maxOperations, nums.copy())
    #
    #         if med_value >= 0:
    #             max_reachable = med - 1
    #         else:
    #             min_reachable = med + 1
    #
    #     return min_reachable

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Helper function to check if a given maximum size 'max_size'
        # is feasible within the allowed number of operations
        def is_feasible(max_size: int) -> bool:
            # Calculate the total number of operations required to make all
            # balls in bags less than or equal to 'max_size'
            total_operations = sum((num - 1) // max_size for num in nums)
            # Check if the total number of operations needed is within
            # the maximum allowed operations
            return total_operations <= maxOperations

        # Find the smallest maximum size of the bags (leftmost position) that
        # requires an equal or lower number of operations than max_operations.
        # The search range is between 1 and the maximum number in 'nums'
        smallest_max_size = bisect_left(range(1, max(nums) + 1), True, key=is_feasible)

        return smallest_max_size + 1

sol = Solution()

print(sol.minimumSize(nums = [9], maxOperations = 2))
print(sol.minimumSize(nums = [2,4,8,2], maxOperations = 4))
print(sol.minimumSize(nums = [7,17], maxOperations = 2))
print(sol.minimumSize(nums = [431,922,158,60,192,14,788,146,788,775,772,792,68,143,376,375,877,516,595,82,56,704,160,403,713,504,67,332,26], maxOperations = 80))
# 129



# 9, 2
# 3, 3, 3

# 13, 3
# 4, 4, 3, 2

# 5, 8, 7
# 5, 4, 4, 7

# 6, 7, 7
# 6, 3, 4, 7

# 13 7, 2
# 20 -> 5, 5, 5, 5


# 2,4,8,2
# 8,4,2,2 / 4 -> max bags = 4 + 4 = 8


# 8 + 4 + 2 + 2 = 16 / 8 = 2
# sum(nums) / (len(nums) + operations) = min reachable element
# filter -> e > min reachable element


# 8 + 4 = 12
# len(nums) = 2



# / 1
# sum = 12
# len(nums) + operations = 3
# sum / (l + o) = 12 / 3 = 4
# 8, 4
# 4, 4, 4

# / 2
# sum = 12
# len(nums) + operations = 4
# sum / (l + o) = 12 / 6 = 3
# 8, 4
# 4, 4, 4
# 4, 4, 2, 2
# or
# 6, 2, 4
# 3, 3, 2, 4

# / 3
# 8 + 4 + 2 + 2
# sum = 16
# len(nums) + operations = 4 + 3 = 7
# sum / (l + o) = 16 / 7 = 2,28... -> 3

# 8 + 4 + 2 + 2 -> 8, 4
# 8, 4
# 5, 3, 4 -> 5, 4   | 1
# 5, 4
# 2, 3, 4  -> 4  | 1
# 3,1 or 2, 2  | 1


# 9, 3, 2, 2 -> 9, 3
# 9, 3

# 7, 2, 3 -> 7, 3 | 1


# 6, 2, 4
# 3, 3, 2, 4
# 3, 3, 2, 2, 2

# /4
# sum = 12
# len(nums) + operations = 6
# sum / (l + o) = 12 / 6 = 2
# 8, 4
# 4, 4, 4
# 2, 2, 4, 4
# 2, 2, 2, 2, 2, 2


# o = 2
# 7, 17
# sum = 24
# l + o = 2 + 2 = 4
# sum / (l + o) = 24 / 4 = 6


# 17, 7

# 11, 6, 7 -> 11, 7 | 1
# 5, 6, 7 -> 7 | 1

# o = 2
# 7, 17, 7
# sum = 31
# l + o = 3 + 2 = 5
# sum / (l + o) = 31 / 5 = 6,2

# 7, 7, 17
# 7, 7, 10, 7 | 1
# 7, 7, 5, 5, 7 | 1



# 922,