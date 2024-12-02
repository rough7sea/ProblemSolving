# class Solution:
#     def kthCharacter(self, k: int) -> str:
#         arr = [0]
#         while len(arr) < k:
#             arr += [(x + 1) % 26 for x in arr]
#         return chr(arr[k - 1] + 97)

class Solution:

    def next_alpha(self, s):
        return chr((ord(s) + 1))

    def update(self, word) -> str:
        if len(word) == 1:
            return word + self.next_alpha(word)
        m = int(len(word) / 2)
        return word + self.update(word[m:])

    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while len(word) < k:
            word = self.update(word)

        print(word)
        return word[k]


sol = Solution()
print(sol.kthCharacter(k=5))
print(sol.kthCharacter(k=31))

# a b c d e f g

# a - 1
# ab - 2
# abbc - 4
# abbc bccd - 8
# abbc bccd bccd cdde - 16
# abbc bccd bccd cdde | bccd cdde cdde deef - 32
# abbc bccd bccd cdde bccd cdde cdde deef


# 64
# 128
# 256
# 512



