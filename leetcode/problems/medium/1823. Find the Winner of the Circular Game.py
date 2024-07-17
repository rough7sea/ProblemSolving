class Solution:

    def findTheWinner_brut_force(self, n: int, k: int) -> int:
        queue = []
        for i in range(n):
            queue.append(i)

        while len(queue) > 1:
            step = k % len(queue)
            while step != 0:
                i = queue.pop(0)
                queue.append(i)
                step -= 1
            queue.pop()

        return queue.pop() + 1

    def findTheWinner(self, n: int, k: int) -> int:
        queue = list(range(1, n + 1))

        index = 0
        while len(queue) > 1:
            index = (index + k - 1) % len(queue)
            queue.pop(index)

        return queue[0]


sol = Solution()
print(sol.findTheWinner(n=5, k=2))
print(sol.findTheWinner(n=8, k=8))


