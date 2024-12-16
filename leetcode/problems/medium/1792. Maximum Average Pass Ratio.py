from heapq import heappush, heappop
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        queue = []
        all_passed = 0
        res = 0

        for i in range(len(classes)):
            passed, total = classes[i]
            if passed == total:
                all_passed += 1
                res += 1
                continue

            p = passed / total
            res += p
            new_p = (passed + 1) / (total + 1)
            heappush(queue, (p - new_p, i))

        if all_passed == len(classes):
            return res / all_passed

        for _ in range(extraStudents):
            diff, i = heappop(queue)
            passed, total = classes[i]
            res -= diff

            passed += 1
            total += 1
            classes[i] = [passed, total]

            p = passed / total
            new_p = (passed + 1) / (total + 1)
            heappush(queue, (p - new_p, i))

        return res / (all_passed + len(queue))


sol = Solution()
print(sol.maxAverageRatio(classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2))
