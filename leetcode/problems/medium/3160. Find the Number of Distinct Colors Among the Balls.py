from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        colorsToFreq = dict()
        numsToColor = dict()
        for num, color in queries:
            if color not in colorsToFreq:
                colorsToFreq[color] = 0
            colorsToFreq[color] += 1

            if num in numsToColor:
                colorsToFreq[numsToColor[num]] -= 1
                if colorsToFreq[numsToColor[num]] == 0:
                    del colorsToFreq[numsToColor[num]]

            numsToColor[num] = color
            res.append(len(colorsToFreq.keys()))

        return res


sol = Solution()
print(sol.queryResults(limit=4, queries=[[1, 4], [2, 5], [1, 3], [3, 4]]))
