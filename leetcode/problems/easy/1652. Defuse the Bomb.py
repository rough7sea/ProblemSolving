from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0 for i in range(len(code))]
        res = []
        sum = 0
        i = 1 if k > 0 else len(code) + k
        for j in range(abs(k)):
            sum += code[i]
            i = self.next(i, len(code))

        s = 1 if k > 0 else len(code) + k
        for j in range(len(code)):
            res.append(sum)
            sum -= code[s]
            s = self.next(s, len(code))
            sum += code[i]
            i = self.next(i, len(code))
        return res

    def next(self, i, n):
        return (i + 1) % n


sol = Solution()
# print(sol.decrypt(code=[5, 7, 1, 4], k=3))
print(sol.decrypt(code=[2, 4, 9, 3], k=-2))
