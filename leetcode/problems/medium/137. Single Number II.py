from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twice = 0

        for el in nums:
            third = twice & el
            twice |= (ones & el)

            ones |= el
            ones &= (~twice & ~third)
            twice &= ~third

        return ones




sol = Solution()
print(sol.singleNumber(nums = [2, 2, 2, 3, 3, 3, 4]))
print(sol.singleNumber(nums = [0,1,0,1,0,1,99]))
print(sol.singleNumber(nums = [2,99,1,2,1,2,1]))
print(sol.singleNumber(nums = [2,3,1,2,1,2,1]))
print(sol.singleNumber(nums = [98,1,98,1,98,1,99]))
print(sol.singleNumber(nums = [98,1,98,1,98,1,3]))
print(sol.singleNumber(nums = [98,98,1,1,98,1,6]))

#ones = 0011
#twos = 1010

# ones&twos = 0010
# ones^ones&twos = 0010
# 0001



# 0 1 0
# 0 1 0
# 0 1 0

# 0 1 1
# 0 1 1
# 0 1 1

# 1 0 0


# 1 0 0


#