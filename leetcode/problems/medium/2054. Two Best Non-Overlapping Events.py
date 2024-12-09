from typing import List


# Sort events by start time. Loop through all events.
# When considering event x: use binary search to find index of first event that starts after x ends.
# Use that index to find max value of all events that starts after x ends.
# To do that precompute max value for all suffixes.

# class Solution:
#
#     def maxTwoEvents(self, events: List[List[int]]) -> int:
#         events.sort(key=lambda x: x[0])
#         maxSum = 0
#         endMaxValue = dict()
#
#         for i in range(len(events)):
#             start, end, value = events[i]
#             curSum = value
#             if start in endMaxValue:
#                 curSum += endMaxValue[start]
#
#             maxSum = max(curSum, maxSum)
#
#
#         return maxSum

#
# Java
# C++
# TypeScript
# from bisect import bisect_right
#
# class Solution:
#     def maxTwoEvents(self, events: List[List[int]]) -> int:
#         # Sort the events based on their start times.
#         events.sort()
#         n = len(events)
#
#         # 'max_value_after' holds the maximum value of any single event from index i to the end.
#         max_value_after = [events[-1][2]] * n
#
#         # Fill 'max_value_after' by iterating from the second last to the first event.
#         for i in range(n - 2, -1, -1):
#             max_value_after[i] = max(max_value_after[i + 1], events[i][2])
#
#         # Initialize maximum value to be zero at the start.
#         max_value = 0
#
#         # Iterate over each event
#         for _, end_time, value in events:
#             # Find the first event that starts after the current event ends.
#             idx = bisect_right(events, end_time, key=lambda x: x[0])
#
#             # If such an event is found, add the value of the current event to
#             # the maximum value found after the current event.
#             if idx < n:
#                 combined_value = value + max_value_after[idx]
#             else:
#                 combined_value = value
#
#             # Update the maximum value with the larger of the two values.
#             max_value = max(max_value, combined_value)
#
#         # Return the maximum value found which could be from two or one events.
#         return max_value


from bisect import bisect_right
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        max_weights = [0]
        max_weight_ends = [-1]

        events.sort(key = lambda x: x[1])

        max_two = 0
        for start, end, weight in events:
            index = bisect_right(max_weight_ends, start - 1) - 1

            if weight + max_weights[index] > max_two:
                max_two = weight + max_weights[index]
            if weight > max_weights[-1]:
                max_weights.append(weight)
                max_weight_ends.append(end)

        return max_two

sol = Solution()
print(sol.maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]))