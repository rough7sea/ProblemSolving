from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        n = len(nums)
        if n < 2:
            return

        if k % n == 0:
            return

        def next(n, i, k) -> int:
            return (i + k) % n

        i = 0
        el = nums[i]
        counter = 0
        shift = 0
        while counter < len(nums):
            counter += 1
            i = next(n, i, k)

            if i == shift:
                shift += 1
                next_el = nums[next(n, shift, 0)]
            else:
                next_el = nums[i]

            nums[i] = el
            el = next_el
            if i == shift - 1:
                i = shift

        pass


sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
sol.rotate(nums=nums, k=3)
print(nums)

nums = [-1, -100, 3, 99]
sol.rotate(nums=nums, k=2)
print(nums)


nums = [1, 2, 3, 4, 5, 6]
sol.rotate(nums=nums, k=3)
print(nums)
