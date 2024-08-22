class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        s_2 = 1
        s_1 = 2
        i = 3
        while i < n:
            t = s_2
            s_2 = s_1
            s_1 = t + s_1
            i += 1
        return s_1 + s_2

        # def climbStairs(self, n: int) -> int:
        #     # let opt[n] stands for the distinct ways I can climb to the top given n steps
        #     # recurrence formula: opt[n] = opt[i-1] + opt[i-2]
        #     # base case: opt[1] = 1, opt[0] = 1
        #
        #     opt = [0] * (n + 1)
        #     opt[0] = 1
        #     opt[1] = 1
        #
        #     for i in range(2, n+1):
        #         opt[i] = opt[i-1] + opt[i-2]  #can be either opt[i-1] plus 1step or opt[i-2] plus 2steps to get to current position
        #         # print('opt['+str(i)+']: ', opt[i])
        #
        #     return opt[n]

sol = Solution()
print(sol.climbStairs(4))
print(sol.climbStairs(5))
print(sol.climbStairs(6))

