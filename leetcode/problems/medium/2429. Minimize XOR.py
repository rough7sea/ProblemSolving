class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        if num1 == num2:
            return num1
        num_1_bits = 0
        num_2_bits = 0

        t = num2
        while t != 0:
            if t & 1 == 1:
                num_2_bits += 1
            t >>= 1

        t = num1
        while t != 0:
            if t & 1 == 1:
                num_1_bits += 1
            t >>= 1

        if num_1_bits == num_2_bits:
            return num1

        if num_1_bits > num_2_bits:
            t = num1
            shifts = 0
            while num_1_bits != num_2_bits:
                if t & 1 == 1:
                    num_1_bits -= 1
                t >>= 1
                shifts += 1

            for _ in range(shifts):
                t <<= 1

            return t

        # num_1_bits < num_2_bits
        t = num1
        shifts = 0
        while num_1_bits != num_2_bits:
            if t & 1 == 0:
                num_2_bits -= 1
            t >>= 1
            shifts += 1

        for _ in range(shifts):
            t <<= 1
            t |= 1

        return t


sol = Solution()
print(sol.minimizeXor(num1 = 3, num2 = 5))
print(sol.minimizeXor(num1 = 1, num2 = 12))
