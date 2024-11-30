from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        stone = "#"
        empty = "."
        obstacle = "*"
        res = [[empty for _ in range(len(box))] for _ in range(len(box[0]))]
        res_i = len(box) - 1
        for i in range(len(box)):
            firstEmpty = None
            for j in range(len(box[i]) - 1, -1, -1):
                if box[i][j] == empty and firstEmpty is None:
                    firstEmpty = j
                    continue

                if box[i][j] == obstacle:
                    res[j][res_i] = obstacle
                    firstEmpty = None
                    continue

                if box[i][j] == stone:
                    if firstEmpty is None:
                        res[j][res_i] = stone
                        continue

                    box[i][firstEmpty] = stone
                    res[firstEmpty][res_i] = stone
                    # box[i][j] = empty
                    firstEmpty -= 1
            res_i -= 1

        return res


sol = Solution()
# print(sol.rotateTheBox(box=[["#", ".", "#"]]))

# print(sol.rotateTheBox(box=[["#", ".", "*", "."],
#                             ["#", "#", "*", "."]]))
#
res = sol.rotateTheBox(box=[
    ["#", "#", "*", ".", "*", "."],
    ["#", "#", "#", "*", ".", "."],
    ["#", "#", "#", ".", "#", "."]
])
for i in range(len(res)):
    print(res[i])
