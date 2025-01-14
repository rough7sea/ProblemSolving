class Solution:
    # def calculate(self, s: str) -> int:
    #     stack = []
    #     i = 0
    #     cur_state = [0]
    #     while i < len(s) or len(cur_state) > 2:
    #         if len(cur_state) > 2:
    #             b = cur_state.pop()
    #             operator = cur_state.pop()
    #             a = cur_state.pop()
    #             if operator == '-':
    #                 cur_state.append(a - b)
    #             elif operator == '+':
    #                 cur_state.append(a + b)
    #             continue
    #
    #         if s[i] == ' ':
    #             i += 1
    #             continue
    #
    #         if s[i] == '(':
    #             stack.append(cur_state)
    #             cur_state = [0]
    #             i += 1
    #             continue
    #
    #         if s[i] == ')':
    #             prev_state = stack.pop()
    #             if len(prev_state) == 1:
    #                 prev_state.append('+')
    #             prev_state.append(cur_state[0])
    #             cur_state = prev_state
    #             i += 1
    #             continue
    #
    #         if s[i] == '-' or s[i] == '+':
    #             cur_state.append(s[i])
    #             i += 1
    #             continue
    #
    #         if s[i].isdigit():
    #             str_digit = ''
    #             while i < len(s) and s[i].isdigit():
    #                 str_digit += s[i]
    #                 i += 1
    #             b = int(str_digit)
    #             if len(cur_state) == 1:
    #                 cur_state.append('+')
    #             cur_state.append(b)
    #
    #     return cur_state[0]

    def calculate(self, s: str) -> int:
        stack = []
        sign, num = 1, 0
        res = 0

        for c in s:
            if c >= '0':
                num = 10 * num + ord(c) - 48
            elif c == '(':
                stack += [res, sign]
                res, sign = 0, 1
                num = 0
            elif c == ')':
                res += sign * num
                res = res * stack.pop() + stack.pop()
                num = 0
            elif c == '+' or c == '-':
                res += sign * num
                sign = 44 - ord(c)  # 43(+) -> 1, 45(-) -> -1
                num = 0

        return res + sign * num

sol = Solution()
print(sol.calculate(s = "(1+(4+5+2)-3)+(6+8)"))