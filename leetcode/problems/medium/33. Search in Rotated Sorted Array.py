from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while right >= left:
            if target == nums[left]:
                return left
            if target == nums[right]:
                return right

            mid_i = left+(right-left)//2
            if target == nums[mid_i]:
                return mid_i

            if nums[left] > nums[mid_i] and (nums[left] < target > nums[mid_i] or target < nums[mid_i]):
                right = mid_i
                left += 1
            elif nums[mid_i] > nums[right] and (target > nums[mid_i] or target < nums[right]):
                left = mid_i
                right -= 1
            else:
                if nums[left] < target < nums[mid_i]:
                    right = mid_i - 1
                    left += 1
                else:
                    left = mid_i + 1
                    right -= 1
        return -1


sol = Solution()
print(sol.search([0, 1, 2, 3, 4, 5, 6], 0))
print(sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print(sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
print(sol.search(nums=[1], target=0))

# 0, 1, 2, 3, 4, 5, 6
# 4, 5, 6, 0, 1, 2, 3
# 6, 0, 1, 2, 3, 4, 5
# 1, 2, 3, 4, 5, 6, 0
# 2, 3, 4, 5, 6, 0, 1
