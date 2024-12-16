import heapq
from heapq import heapify, heappush, heappop
from math import sqrt
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        rev_gifts = []
        for el in gifts:
            rev_gifts.append(-el)

        heapify(rev_gifts)
        while k > 0:
            g = heappop(rev_gifts)
            heappush(rev_gifts, -int(sqrt(-g)))
            k -= 1
        res = 0
        for el in rev_gifts:
            res += -el

        return res


sol = Solution()
print(sol.pickGifts(gifts=[25, 64, 9, 4, 100], k=4))
