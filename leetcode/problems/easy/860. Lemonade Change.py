from typing import List


class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for d in bills:
            if d == 5:
                five += 1
            elif d == 10:
                if five > 0:
                    ten += 1
                    five -= 1
                else:
                    return False
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five > 2:
                    five -= 3
                else:
                    return False
        return True


sol = Solution()
print(sol.lemonadeChange(bills=[5, 5, 5, 10, 20]))
print(sol.lemonadeChange(bills=[5, 5, 10, 10, 20]))
