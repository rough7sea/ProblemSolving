from typing import List


class Solution:
    # def subsetXORSum(self, nums: List[int]) -> int:
    #     print(int('1100', 2) * 4)
    #     # for e in nums:
    #     #     print(bin(28))
    #     return 0

    # def subsetXORSum(self, nums: List[int]) -> int:
    #     def dfs(index, current_xor):
    #         # Base case: when all elements have been considered
    #         print(f'index = {index} xor = {bin(current_xor)}')
    #         if index == len(nums):
    #             return current_xor
    #         # Include nums[index] in the subset
    #         include = dfs(index + 1, current_xor ^ nums[index])
    #         # Exclude nums[index] from the subset
    #         exclude = dfs(index + 1, current_xor)
    #         return include + exclude
    #
    #     return dfs(0, 0)

    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        all_or=0
        for i in range(n):
            all_or|=nums[i]
            print(bin(all_or))
        return all_or*(1<<(n-1))
# 0 - 0 = 0
# 0 - 1 = 1
# 1 - 0 = 1
# 1 - 1 = 0


# res - 28
# 11100

# Input: nums = [5,1,6]
# Output: 28
# Explanation: The 8 subsets of [5,1,6] are:
# - The empty subset has an XOR total of 0. 000
# - [5] has an XOR total of 5. - 101
# - [1] has an XOR total of 1. - 001
# - [6] has an XOR total of 6. - 110
# - [5,1] has an XOR total of 5 XOR 1 = 4. 100
# - [5,6] has an XOR total of 5 XOR 6 = 3. 011
# - [1,6] has an XOR total of 1 XOR 6 = 7. 111
# - [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.  010
# 0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28  -  11100

# 101 + 001 + 110 = 101 + 111 = 1100

# 2**len(nums)-1


sol = Solution()
print(sol.subsetXORSum([5, 1, 6]))
