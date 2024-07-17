class Solution:
    # def maximumGain(self, s: str, x: int, y: int) -> int:
    #     x_p = 'ab'
    #     y_p = 'ba'
    #
    #     strat = []
    #     if x > y:
    #         strat.append([x_p, x])
    #         strat.append([y_p, y])
    #     else:
    #         strat.append([y_p, y])
    #         strat.append([x_p, x])
    #
    #     count, s = self.p(s, strat)
    #     return count + self.p(s, strat)[0]
    #
    # def p(self, s, strat):
    #     count = 0
    #     i = 1
    #     f_p, f_c = strat.pop(0)
    #     while i < len(s):
    #         while i < len(s) and s[i] == f_p[1]:
    #             if i > 0 and s[i - 1] == f_p[0]:
    #                 s = s[0:i - 1] + s[i + 1:]
    #                 count += f_c
    #                 i -= 1
    #             else:
    #                 i += 1
    #         i += 1
    #     return [count, s]

    def maximumGain(self, s: str, x: int, y: int) -> int:
        letter_a = "a"
        if x < y:
            # change the role of 'a' and 'b'
            letter_a = "b"
            x, y = y, x

        total = 0
        dxy = x-y
        ab_count = a_count = b_count = 0

        for char in s:
            if char not in "ab":
                if b_count > a_count:
                    a_count, b_count = b_count, a_count
                if a_count > 0:
                    total += ab_count*dxy+b_count*y
                    ab_count = a_count = b_count = 0

            elif char == letter_a:
                a_count += 1

            else:
                # last letter is b.
                # form ab if there is free a
                # or change ba to b + ab
                b_count += 1
                if a_count > ab_count:
                    ab_count += 1

        total += ab_count*dxy+min(a_count, b_count)*y

        return total


sol = Solution()
print(sol.maximumGain(s="cdbcbbaaabab", x=4, y=5))

# x=4, y=5
# cdbcb ba aa ba b + 10
# cdbc ba ab + 9
# cdbc

# x = 5, y = 4
# aabbaaxybbaabb
# a ab baaxybba ab b + 10
# ab aaxybb ab + 10
# aaxybb + 10


# ba > ab
# a ba ba b

# ab > ba
# ab ab ab


# aabbaaxybbaabb
# a ab baaxybbaabb
# ab aaxybbaabb
# aaxybba ab b
# aaxybb ab
# aaxybb