from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def rec(open, close, temp: list[str]):
            if open == 0 and close == 0:
                res.append(''.join(temp))
                return

            if open > 0:
                copy = temp.copy()
                copy.append('(')
                rec(open - 1, close, copy)

            if close > 0 and open < close:
                copy = temp.copy()
                copy.append(')')
                rec(open, close - 1, copy)

        rec(n, n, [])
        return res

sol = Solution()
print(sol.generateParenthesis(3))
