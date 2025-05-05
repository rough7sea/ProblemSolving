from typing import Generator


class Solution:

    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        r_to_l = [0] * n
        l_to_r = [0] * n

        self.calc_force(dominoes, n, r_to_l, 'R', 'L', (v for v in range(n)))
        self.calc_force(dominoes, n, l_to_r, 'L', 'R', (v for v in range(n-1, -1, -1)))

        print(r_to_l)
        print(l_to_r)

        res = []
        for i in range(n):
            if l_to_r[i] == r_to_l[i]:
                res.append(dominoes[i])
                continue

            if l_to_r[i] == 0:
                res.append('R')
                continue

            if r_to_l[i] == 0:
                res.append('L')
                continue

            if l_to_r[i] > r_to_l[i]:
                res.append('R')
            else:
                res.append('L')

        return ''.join(res)

    def calc_force(self, dominoes, n, force_array: list, right: str, left: str, iterator: Generator[int, None, None]):
        prev = ''
        force = 0
        for i in iterator:
            if dominoes[i] == prev:
                force = 0
            elif prev == right and dominoes[i] != left:
                force += 1
            if dominoes[i] == left:
                force = 0
                prev = left
            elif dominoes[i] == right:
                prev = right
            force_array[i] = force


sol = Solution()
# print(sol.pushDominoes(dominoes=".L.R...LR..L.."))
# print(sol.pushDominoes(dominoes="RR.L"))
print(sol.pushDominoes(dominoes=".L.R."))



