from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        visited = {}
        for first in range(len(arr) - 1):
            second = first + 1
            third = first + 2

            while third < len(arr):
                if arr[first] + arr[second] == arr[third]:
                    if (first, second) in visited:
                        count = visited[(first, second)]
                        if (second, third) in visited:
                            visited[(second, third)] = max(count + 1, visited[(second, third)])
                        else:
                            visited[(second, third)] = count + 1
                    else:
                        visited[(second, third)] = 3
                    second += 1
                    third += 1
                    continue

                if arr[third] < arr[first] + arr[second]:
                    third += 1
                elif arr[third] > arr[first] + arr[second]:
                    second += 1
                    if third == second:
                        third += 1
        if not visited:
            return 0
        return max(visited.values())

    # def lenLongestFibSubseq(self, arr: List[int]) -> int:
    #     cache = set()
    #     n = len(arr)
    #     dp = {}
    #     for i in range(n):
    #         for j in range(i - 1, -1, -1):
    #             tar = arr[i] - arr[j]
    #             if tar >= arr[j]:
    #                 break
    #             if tar in cache:
    #                 if (tar, arr[j]) not in dp:
    #                     dp[(arr[j], arr[i])] = 3
    #                 else:
    #                     dp[(arr[j], arr[i])] = dp[(tar, arr[j])] + 1
    #         cache.add(arr[i])
    #
    #     if not dp:
    #         return 0
    #     return max(dp.values())


sol = Solution()
print(sol.lenLongestFibSubseq(arr=[1, 2, 3, 4, 5, 6, 7, 8]))
print(sol.lenLongestFibSubseq(arr=[1, 3, 7, 11, 12, 14, 18]))
