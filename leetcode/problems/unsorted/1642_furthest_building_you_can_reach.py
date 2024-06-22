from typing import List


class Solution:

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        print(f'heights = {heights}, bricks = {bricks}, ladders = {ladders}')
        if len(heights) < 2:
            return 0

        used_ladder_diff = SortedArray()
        used_bricks = 0

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue

            if ladders == 0:
                used_bricks += diff
                if used_bricks > bricks:
                    return i
                continue

            if used_ladder_diff.size() < ladders:
                used_ladder_diff.add(diff)
                continue

            current_min = used_ladder_diff.get_min()

            if diff <= current_min:
                used_bricks += diff
                if used_bricks > bricks:
                    return i
                continue

            used_ladder_diff.remove_min()
            used_ladder_diff.add(diff)

            used_bricks += current_min
            if used_bricks > bricks:
                return i

        return len(heights) - 1


class SortedArray:
    def __init__(self, array=None):
        if array is None:
            self.array = []
        else:
            self.array = array

    def size(self):
        return len(self.array)

    def add(self, value):
        if len(self.array) < 1:
            self.array.append(value)
            return

        if len(self.array) == 1:
            if self.array[0] > value:
                self.array.insert(0, value)
            else:
                self.array.append(value)
            return
        left = self.__binary_search(value)
        self.array.insert(left, value)

    # return value before each must be inserted current
    def __binary_search(self, x):
        left = 0
        right = len(self.array) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # Check if x is present at mid
            if self.array[mid] == x:
                return mid
            # If x is greater, ignore left half
            elif self.array[mid] < x:
                left = mid + 1
            # If x is smaller, ignore right half
            else:
                right = mid - 1
        # If we reach here, then the element
        # was not present
        return left

    def remove_min(self):
        return self.array.pop(0)

    def get_min(self):
        return self.array[0]


solution = Solution()
# array = [14, 3, 19, 3, 6, 9]
# array.sort()
# print(array)
# sorted_array = SortedArray(array)
# print(sorted_array.add(5))
# print(sorted_array.array)
# print(sorted_array.add(7))
# print(sorted_array.array)
# print(sorted_array.add(30))
# print(sorted_array.array)
# print(sorted_array.add(5))
# print(sorted_array.array)
# print(sorted_array.add(2))
# print(sorted_array.array)
print(solution.furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1))
print(solution.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2))
print(solution.furthestBuilding([14, 3, 19, 3], 17, 0))
