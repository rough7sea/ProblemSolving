from typing import List


# Calculate the sum of each subarray of length k
# Use some data structure to store the best subarray from the left and the right
# Iterate over the array to find the best mid subarray


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        best_sum = [[0] * (n + 1) for _ in range(4)]
        best_index = [[0] * (n + 1) for _ in range(4)]

        for t in range(1, 4):
            for i in range(k * t, n + 1):
                current_sum = (
                        prefix_sum[i] - prefix_sum[i - k] + best_sum[t - 1][i - k]
                )

                if current_sum > best_sum[t][i - 1]:
                    best_sum[t][i] = current_sum
                    best_index[t][i] = i - k
                else:
                    best_sum[t][i] = best_sum[t][i - 1]
                    best_index[t][i] = best_index[t][i - 1]

        result = [0] * 3
        end = n
        for t in range(3, 0, -1):
            result[t - 1] = best_index[t][end]
            end = result[t - 1]

        return result


sol = Solution()
# print(sol.maxSumOfThreeSubarrays(nums=[7, 7, 1, 2, 6, 7, 5, 1], k=2))
print(sol.maxSumOfThreeSubarrays(nums=[1, 2, 1, 2, 6, 7, 5, 1], k=2))
# print(sol.maxSumOfThreeSubarrays(nums=[1, 2, 1, 2, 6, 7, 8, 8], k=2))
