class Solution:

    def passThePillow(self, n: int, time: int) -> int:
        f_c = (n - 1) * 2
        o_w_t = time % f_c

        if o_w_t < n:
            return o_w_t + 1

        return n - (o_w_t - n) - 1

# 1 2 3 4 5 6 7 8


sol = Solution()
print(sol.passThePillow(n=4, time=5))  # 2
print(sol.passThePillow(n=3, time=2))  # 3
print(sol.passThePillow(n=8, time=9))  # 6
print(sol.passThePillow(n=18, time=38))  # 5

