class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ''
        for i in range(len(s)):
            num += f'{(ord(s[i]) - 96)}'
        for i in range(k):
            temp = 0
            for n in num:
                temp += int(n)
            num = f'{temp}'
        return int(num)
            