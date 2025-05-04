from typing import List


class Solution:

    def next(self, i, n) -> int:
        return i % n

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        same = set()
        res = 0


        # 0 1 0 0 1 0 1 0 1
        for i in range(1, k):
            prev = self.next(i - 1, n)
            if colors[self.next(i, n)] == colors[prev]:
                same.add(prev)


        for i in range(len(colors)):
            if not same:
                res += 1

            if i in same:
                same.remove(i)

            next_i = self.next(i + k, n)
            tail_i = self.next(i + k - 1, n)
            if colors[next_i] == colors[tail_i]:
                same.add(tail_i)

        return res

sol = Solution()
print(sol.numberOfAlternatingGroups(colors = [0,1,0,1,0], k = 3))
print(sol.numberOfAlternatingGroups(colors = [0,1,0,0,1,0,1], k = 6))
print(sol.numberOfAlternatingGroups(colors = [1,1,0,1], k = 4))