import random
from typing import List


def quicksort(arr, start, stop):
    if (start < stop):
        pivotindex = partitionrand(arr, start, stop)
        quicksort(arr, start, pivotindex - 1)
        quicksort(arr, pivotindex + 1, stop)


def partitionrand(arr, start, stop):
    randpivot = random.randrange(start, stop)

    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)


def partition(arr, start, stop):
    pivot = start  # pivot
    i = start + 1  # a variable to memorize where the
    # partition in the array starts from.
    for j in range(start + 1, stop + 1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1
    return pivot


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return

        i = len(nums) - 1
        while True:
            if i == 0:
                nums.reverse()
                return

            cur = nums[i]
            prev = i - 1

            if cur <= nums[prev]:
                i -= 1
                continue

            # prev < cur,  prev - to change
            s_min = i
            i += 1
            while i < len(nums):
                if nums[s_min] > nums[i] > nums[prev]:
                    s_min = i
                i += 1

            t = nums[s_min]
            nums[s_min] = nums[prev]
            nums[prev] = t

            quicksort(nums, prev + 1, len(nums) - 1)
            return


nums = [1, 3, 2]
sol = Solution()
sol.nextPermutation(nums)
print(nums)
