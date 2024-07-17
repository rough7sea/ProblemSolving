from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        total_flips = 0
        i = 0
        flips_map = [0] * (len(nums) + 1)
        cur_flip = 0
        while i + k <= len(nums):
            cur_flip -= flips_map[i]
            if cur_flip % 2 != nums[i]:
                i += 1
                continue

            flips_map[i + k] = 1
            cur_flip += 1
            total_flips += 1
            i += 1

        while i < len(nums):
            cur_flip -= flips_map[i]
            if (nums[i] == 1 and cur_flip % 2 == 0) or (nums[i] == 0 and cur_flip % 2 == 1):
                i += 1
            else:
                return -1
        return total_flips


sol = Solution()
print(sol.minKBitFlips(nums=[0, 0, 0, 1, 0, 1, 1, 0], k=3))
print(sol.minKBitFlips(nums=[1, 0, 1, 0, 1, 0, 1, 1], k=3))
print(sol.minKBitFlips(nums=[1, 1, 1, 1, 1, 1, 1, 0], k=3))
print(sol.minKBitFlips(nums=[0, 1, 0], k=1))

# Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
# Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
# Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]


# 1, 0, 1, 0, 1, 0, 1, 1

# 1, 1, 0, 1, 1, 0, 1, 1
# 1, 1, 1, 0, 0, 0, 1, 1
# 1, 1, 1, 1, 1, 1, 1, 1

# 1, 1, 1, 1, 1, 1, 1, 0
