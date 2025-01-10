from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff_array = [0] * len(s)

        for start, end, direction in shifts:
            if direction == 0:
                diff_array[start] -= 1
                if end < len(s) - 1:
                    diff_array[end + 1] += 1
            else:
                diff_array[start] += 1
                if end < len(s) - 1:
                    diff_array[end + 1] -= 1
        res = ''
        diff = 0
        for i in range(len(s)):
            diff += diff_array[i]
            res += chr((97 + (ord(s[i]) - 97 + diff) % 26))
        return res


sol = Solution()
# print(sol.shiftingLetters(s="abc", shifts=[[0, 1, 0], [1, 2, 1], [0, 2, 1]]))
print(sol.shiftingLetters(s="dztz", shifts=[[0, 0, 0], [1, 1, 1]]))
