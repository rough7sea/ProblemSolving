class Solution:
    # def rangeBitwiseAnd(self, left: int, right: int) -> int:
    #     if left == right:
    #         return left
    #
    #     bin_left = bin(left)
    #     bin_right = bin(right)
    #     if len(bin_right) != len(bin_left):
    #         return 0
    #
    #     r = []
    #     for i in range(2, len(bin_left)):
    #         if bin_right[i] == bin_left[i]:
    #             r.append(bin_right[i])
    #         else:
    #             break
    #     return int(''.join(r) + '0' * (len(bin_left) - i), 2)

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left

        # find the right-most common bit
        counter = 0
        while left != right:
            left >>= 1
            right >>= 1
            counter += 1
        #print(f"{bin(left)} {bin(right)} {counter}")

        # fill it with zeroes
        left <<= counter

        return left

        # 001000100
        # 000000001




sol = Solution()
print(sol.rangeBitwiseAnd(4, 7))
print(sol.rangeBitwiseAnd(1, 1))
print(sol.rangeBitwiseAnd(10, 11))

# 0010 - 2
# 0011 - 3
# 0100 - 4
# 0101 - 5
# 0110 - 6
# 0111 - 7
# 1000 - 8