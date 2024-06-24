from curses.ascii import isdigit


class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        orient = True

        if i < len(s):
            if s[i] == '-':
                i += 1
                orient = False
            elif s[i] == '+':
                i += 1

        # minimum value of -2,147,483,648 and a maximum value of 2,147,483,647 (inclusive)

        if i < len(s) and isdigit(s[i]):
            end = i
            while end < len(s) and isdigit(s[end]):
                end += 1
            value = int(s[i:end])

            if not orient:
                if value > 2147483648:
                    value = 2147483648
                value = -value
            else:
                if value > 2147483647:
                    value = 2147483647
            return value

        return 0


sol = Solution()
print(sol.myAtoi('f   1233f4 '))

