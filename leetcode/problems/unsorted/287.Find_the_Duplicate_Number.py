import array
from typing import List


# S = (n/2) * (a + b), где S – сумма всех чисел, n – количество чисел, a – первое число, b – последнее число

class BitMap:
    BITMASK = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]

    def __init__(self, maxnum=0):
        """
        Create a BitMap
        """
        nbytes = (maxnum + 7) // 8
        self.bitmap = array.array('B', [0 for i in range(nbytes)])

    def set(self, pos):
        """
        Set the value of bit@pos to 1
        """
        self.bitmap[pos // 8] |= self.BITMASK[pos % 8]

    def test(self, pos):
        """
        Return bit value
        """
        return (self.bitmap[pos // 8] & self.BITMASK[pos % 8]) != 0


class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        # 100000 - max
        bm = BitMap(len(nums))
        for i in nums:
            if bm.test(i):
                return i
            bm.set(i)

        return 0


sol = Solution()
print(sol.findDuplicate([1, 2, 3, 4, 5, 6, 7, 7]))
print(sol.findDuplicate([1, 2, 3, 4, 5, 6, 6, 7]))
print(sol.findDuplicate([1, 1, 2, 3, 4, 5, 6]))
print(sol.findDuplicate([1, 2, 3, 4, 4, 5, 6]))
print(sol.findDuplicate([1, 4, 4, 2, 4]))
