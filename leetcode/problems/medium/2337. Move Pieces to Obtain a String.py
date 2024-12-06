class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s_r_count = 0
        s_l_count = 0

        t_r_count = 0
        t_l_count = 0

        for i in range(len(target)):
            s = start[i]
            t = target[i]

            if t == 'L':
                t_l_count += 1
            elif t == 'R':
                t_r_count += 1

            if s == 'L':
                s_l_count += 1
            elif s == 'R':
                s_r_count += 1

            if t_l_count > 0 and s_r_count > 0 or t_r_count > 0 and s_l_count > 0:
                return False

            if s_l_count > t_l_count or t_r_count > s_r_count:
                return False

            if t_l_count > 0 and s_l_count > 0:
                t_l_count -= 1
                s_l_count -= 1

            if t_r_count > 0 and s_r_count > 0:
                t_r_count -= 1
                s_r_count -= 1

        return s_r_count == 0 and s_l_count == 0 and t_r_count == 0 and t_l_count == 0

sol = Solution()
# print(sol.canChange(start = "_L__R__R_", target = "L______RR"))
# print(sol.canChange(start = "R_L_", target = "LR__"))
print(sol.canChange(start = "R_L_", target = "__LR"))

# ___LL___ = s
# ____LL__ = t

# ___RR___ = s
# __RR____ = t

# ___RR___ = s
# ____RR__ = t

# _L__R__R_ = s
# L______RR = t

# s = __RL__R_
# t = ___RL__R

# __LR___ = s
# ___LR__ = t

# ___RLR___ = s
# __RLR____ = t
