from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        visited = [False] * len(arr)
        windows = 0
        j = 0
        max_visited = arr[0]

        for i in range(len(arr)):
            max_visited = max(max_visited, arr[i])
            visited[arr[i]] = True

            while j < len(arr) and visited[j]:
                j += 1

            if max_visited <= j - 1:
                windows += 1

        return windows


sol = Solution()
print(sol.maxChunksToSorted([0, 3, 1, 2]))
print(sol.maxChunksToSorted([3, 1, 0, 2, 5, 6, 4, 9, 7, 8]))
print(sol.maxChunksToSorted([0, 1, 2, 3, 4]))
print(sol.maxChunksToSorted(arr=[4, 3, 2, 1, 0]))
