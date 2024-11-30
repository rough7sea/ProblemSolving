from collections import deque


def replace(s: str, index: int):
    return s[:index] + s[index + 1:]


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_par_to_remove = deque()
        par_to_remove = []

        for i in range(len(s)):
            e = s[i]
            if e != ')' and e != '(':
                continue

            if e == '(':
                open_par_to_remove.append(i)
            else: # ')'
                if len(open_par_to_remove) > 0:
                    open_par_to_remove.pop()
                else: # ')' to remove
                    par_to_remove.append(i)

        if len(open_par_to_remove) > 0:
            par_to_remove.extend(open_par_to_remove)
            par_to_remove.sort()

        # i = len(par_to_remove) - 1
        # result = ""
        # for y in reversed(range(len(s))):
        #     if i >= 0 and par_to_remove[i] == y:
        #         i -= 1
        #         continue
        #     result = s[y] + result
        # return result

        for e in reversed(par_to_remove):
            s = replace(s, e)

        return s


s = "(lee))(t(c)o)de)("
sol = Solution()
print(sol.minRemoveToMakeValid(s))
