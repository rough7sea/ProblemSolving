class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        a = ['a', 'b', 'c']

        count = 0
        q = ['']

        while True:
            s = q.pop(0)

            for c in a:
                if len(s) == 0 or s[-1] != c:
                    s_n = s + c
                    if len(s_n) == n:
                        count += 1
                    elif len(s_n) > n:
                        return ''

                    if count == k:
                        return s_n

                    q.append(s_n)
        return ''


sol = Solution()
print(sol.getHappyString(1, 3))
print(sol.getHappyString(1, 4))
print(sol.getHappyString(3, 9))
