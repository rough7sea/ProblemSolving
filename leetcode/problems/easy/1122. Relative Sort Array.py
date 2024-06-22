import array
from typing import List, Dict


def calculateMap(arr1: List[int]) -> dict[int, int]:
    map: dict[int, int] = {}
    for e in arr1:
        if e not in map:
            map[e] = 1
        else:
            map[e] += 1
    return map


class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        map1 = calculateMap(arr1)
        result = []
        for e in arr2:
            freq = map1[e]
            for i in range(freq):
                result.append(e)
            del map1[e]
        for k in sorted(map1.keys()):
            freq = map1[k]
            for i in range(freq):
                result.append(k)
        return result


sol = Solution()
print(sol.relativeSortArray(arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]))
