from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        map = {}
        str = ''
        if len(arr) < 2 or m >= len(arr):
            return False

        for i in range(len(arr)):
            if i + 1 < m:
                str += f'{arr[i]}'
            else:
                if len(str) < m:
                    str += f'{arr[i]}'
                else:
                    str = str[1:] + f'{arr[i]}'
                if str in map:
                    end = map[str][1]
                    if end + m == i:
                        map[str][0] += 1
                        map[str][1] = i
                    elif end + m < i:
                        map[str][0] = 1
                        map[str][1] = i

                    if map[str][0] == k:
                        return True

                else:
                    map[str] = [1, i]

        return False


sol = Solution()
print(sol.containsPattern(arr=[1, 2, 3, 1, 2], m=2, k=2))
print(sol.containsPattern(arr=[1, 2, 1, 2, 1, 1, 1, 3], m=2, k=2))
print(sol.containsPattern(arr=[2, 2], m=1, k=2))
print(sol.containsPattern(arr=[2, 1, 2, 2, 2, 2, 2, 2], m=2, k=2))

#
# we need to have pattern in adjacent manner, its written "consecutive" in question.
#
# [1,2,3,1,2] in this 3 comes in-between, so false
# [1,2,1,2,3] , its true as [1,2] is adjacent/consecutive to [1,2]
