import bisect


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        if (locked[0] == "1" and s[0] == ")") or (locked[-1] == "1" and s[-1] == "("):
            return False

        stack_open = []
        stack_changeable = []

        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == '(':
                    stack_open.append(i)
                else:
                    if stack_open:
                        stack_open.pop()
                    elif stack_changeable:
                        stack_changeable.pop()
                    else:
                        return False
            else:
                stack_changeable.append(i)

        if len(stack_open) == 0:
            return True

        if len(stack_open) > len(stack_changeable):
            return False

        x = bisect.bisect_left(stack_changeable, stack_open[0])

        if x >= len(stack_changeable):
            return False

        for i in range(x, len(stack_changeable)):
            if stack_changeable[i] > stack_open[0]:
                stack_open.pop(0)
                if len(stack_open) == 0:
                    break

        return len(stack_open) == 0


sol = Solution()
print(sol.canBeValid(s = "))()))", locked = "010100"))
print(sol.canBeValid(s = "))()))", locked = "110100"))
print(sol.canBeValid(s = "()()", locked = "0000"))
print(sol.canBeValid(s =
                     "())()))()(()(((())(()()))))((((()())(())",
                     locked =
                     "1011101100010001001011000000110010100101"))
print(sol.canBeValid(s =
                     "())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(",
                     locked =
                     "100011110110011011010111100111011101111110000101001101001111"))
