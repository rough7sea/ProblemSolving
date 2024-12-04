from typing import List


class Solution:
    # def addSpaces(self, s: str, spaces: List[int]) -> str:
    #     index, result = 0, []
    #
    #     for space in spaces:
    #         result.append(s[index : space])
    #         index = space
    #
    #     result.append(s[index :])
    #     return " ".join(result)

    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # for space in spaces[::-1]:
        #     s = s[:space] + ' ' + s[space:]
        # return s
        res = ''
        j = len(spaces) - 1
        for i in range(len(s) - 1, -1, -1):
            res += s[i]
            if i == spaces[j]:
                res += ''
                j -= 1
        return res[::-1]


sol = Solution()
print(sol.addSpaces(s="LeetcodeHelpsMeLearn", spaces=[8, 13, 15]))
