from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        new_array = arr.copy()
        new_array.sort()
        c = {}
        count = 1
        for i in range(len(new_array)):
            val = new_array[i]
            if val not in c:
                c[val] = count
                count += 1
        res = []
        for e in arr:
            res.append(c[e])
        return res

        # # Create a sorted list of the unique elements in arr
        # sorted_unique = sorted(set(arr))
        #
        # # Create a dictionary to map each element to its rank
        # rank_dict = {value: rank + 1 for rank, value in enumerate(sorted_unique)}
        #
        # # Replace each element in arr with its rank
        # return [rank_dict[element] for element in arr]


sol = Solution()
print(sol.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]))
