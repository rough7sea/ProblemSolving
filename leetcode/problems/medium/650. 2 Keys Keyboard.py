from typing import List


class Solution:
    def minSteps(self, n: int) -> int:
        nums = self.primfacs(n)
        nums.sort(reverse=True)
        res = 0
        for e in nums:
            if e % 2 == 0:
                res += e
            else:
                if res == 0:
                    res += e
                else:
                    res += e
        return res

    def primfacs(self, n: int) -> List[int]:
        i = 2
        primfac = []
        while i * i <= n:
            while n % i == 0:
                primfac.append(i)
                n = n / i
            i = i + 1
        if n > 1:
            primfac.append(int(n))
        return primfac


sol = Solution()
print(sol.minSteps(7))
print(sol.minSteps(47))
print(sol.minSteps(48))
# АА АА АА АА
# AA c p
# AAAA c p
# AAAAAAAA c p
# AAAAAAAAAAAAAAAA c p

# AAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAA c p p p
# AAA AAA AAAAAA AAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAA  c p p  cp cp cp cp
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

print(sol.minSteps(55))
# ААААА ААААА ААААА ААААА ААААА ААААА ААААА ААААА ААААА ААААА ААААА

# c p p p p c p p p p p p p p p p
# ААААААААААА ААААААААААА ААААААААААА ААААААААААА ААААААААААА

# AAAAA

# A
# AA
# AAA
# AAAA
# AAAAA




# AAAAAA

# AA AA AA  - c p c p p
# AAA AAA -   c p p c p


# AAAAAAA
# c p p p p p p

# AA AA AA AA - c p c p p p
# AA AA AA AA - c p c p c p
# AA AA AA AA - c p p p c p

# AAA AAA AAA
# c p p c p p


