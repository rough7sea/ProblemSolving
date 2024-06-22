from typing import List


def fundAll(s: str, e: str) -> [int]:
    for i in range(len(s)):
        s[i]
    # pass


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        int_dict = []
        extra = 0

        dictionary.sort(key=lambda x: len(x), reverse=True)

        print(dictionary)

        for e in dictionary:
            find = s.find(e)
            # entrance = fundAll(s, e)
            if find == -1:
                continue
        #
            size = find + len(e)
            if find == 0 and size == len(s):
                return 0
            # int_dict.append([find, size])
        #
        # int_dict.sort()
        # print(int_dict)

        return extra


sol = Solution()
print(sol.minExtraChar(s="leetscode", dictionary=[
    "leet", "code", "leetcode", "tsc", "tscode", "eetsc", "sc", "e"
]))

# 'deeeeeeee'
# ['deeeeeee', 'e']


#  seeee
#  eeee, se