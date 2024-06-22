class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        size = len(s)
        zag_count = numRows - 2

        result = ''

        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                num = i
                while num <= size - 1:
                    result += s[num]
                    num += numRows + zag_count
                continue

            if i > size - 1:
                break
            num = i
            result += s[num]

            while num < size - 1:
                zag_shift = i * 2
                num += numRows + zag_count - zag_shift
                if num > size - 1:
                    break
                result += s[num]

                num += zag_shift
                if num > size - 1:
                    break
                result += s[num]

        return result


sol = Solution()
# print(sol.convert("PAYPALISHIRING", 4))
print(sol.convert("A", 4))


# Input: s = "PAYP AL ISHI RI NG", numRows = 4
# Output: "PIN ALSIG YAHR PI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I