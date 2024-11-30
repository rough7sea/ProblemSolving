from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        for i in range(1, len(arr) - 1):
            if not (
                    arr[i - 1] < arr[i] < arr[i + 1] or
                    arr[i - 1] > arr[i] > arr[i + 1] or
                    arr[i - 1] < arr[i] > arr[i + 1]
            ):
                return False
        return True



