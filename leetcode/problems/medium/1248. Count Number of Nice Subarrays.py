from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        oddCount = 0
        leftC = 1
        rightC = 1
        left = 0
        right = 0
        while left <= right:
            while oddCount != k:
                if right == len(nums):
                    break
                if nums[right] % 2 == 1:  # odd
                    oddCount += 1
                right += 1

            if oddCount == k:
                while oddCount == k:
                    if nums[left] % 2 == 1:  # odd
                        oddCount -= 1
                    else:
                        leftC += 1
                    left += 1
                    if left == right:
                        break
                while right < len(nums) and nums[right] % 2 != 1:
                    right += 1
                    rightC += 1
                    if right == len(nums):
                        return res + leftC * rightC

                res += leftC * rightC
                leftC = 1
                rightC = 1
            else:
                break
        return res


sol = Solution()
print(sol.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
print(sol.numberOfSubarrays([1, 1, 2, 1, 1], 3))
print(sol.numberOfSubarrays([2, 4, 6], 1))
