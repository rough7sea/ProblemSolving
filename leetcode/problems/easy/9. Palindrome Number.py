import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        digits = int(math.log10(x)) + 1

        n = x
        while True:
            d = pow(10, digits - 1)
            left = int(n / d)
            right = n % 10
            n = int(n % d / 10)
            digits -= 2
            if left != right:
                return False

            if digits <= 1:
                return True


sol = Solution()
print(sol.isPalindrome(112321))
