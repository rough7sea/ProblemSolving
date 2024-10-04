from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        vals = dict()
        for i in range(len(arr)):
            num = arr[i] % k
            diff = k - num
            if diff in vals:
                vals[diff] -= 1
                if vals[diff] == 0:
                    vals.pop(diff)
            else:
                if num in vals:
                    vals[num] += 1
                else:
                    vals[num] = 1
        vals.pop(0, 0)
        return len(vals) == 0


sol = Solution()
print(sol.canArrange(arr=[1, 2, 3, 4, 5, 10, 6, 7, 8, 9], k=5))
