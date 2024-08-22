class Solution:
    # def findComplement(self, num: int) -> int:
    #     print('{0:b}'.format(num))
    #     print(('1'*len('{0:b}'.format(num))))
    #     print(int(('1'*len('{0:b}'.format(num)))))
    #     return num ^ int('1'*len('{0:b}'.format(num)), 2)


    def findComplement(self, num: int) -> int:
        res = ''
        b__format = '{0:b}'.format(num)
        print(b__format)
        for i in b__format:
            if i == '0':
                res += '1'
            else:
                res += '0'
        print(res)
        return int(res, 2)





sol = Solution()
print(sol.findComplement(5))
#
# print(2 ** 31)
# print(bin(2147483647))
#
# a = "11011111101100110110011001011101000"
# b = "11111111111111111111111111111111111"
# y = int(a, 2) ^ int(b, 2)
# print('{0:b}'.format(y))

# print(len('{0:b}'.format(5)))
