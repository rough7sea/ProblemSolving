from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit() or (len(token) > 1 and token[0] == '-'):
                stack.append(int(token))
                continue

            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
        return int(stack.pop())

sol = Solution()
# print(sol.evalRPN(tokens = ["4","13","5","/","+"]))
print(sol.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))