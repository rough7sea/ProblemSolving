class Solution:
    def minSwaps(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        left_opened = 0
        right_closed = 0

        swap = 0

        # ']' - closed
        # '[' - opened

        while right > left:
            if s[left] == '[':
                left_opened += 1
                left += 1
                continue

            # ']'
            if left_opened > 0:
                left_opened -= 1
                left += 1
                continue
            while right > left:
                if s[right] == ']':
                    right_closed += 1
                    right -= 1
                    continue
                # '['
                if right_closed > 0:
                    right_closed -= 1
                    right -= 1
                    continue
                left_opened += 1
                swap += 1
                right -= 1
                break
            left += 1
        return swap


sol = Solution()
print(sol.minSwaps("[]]][][][[]["))
print(sol.minSwaps("]]][[["))
print(sol.minSwaps("][]["))
