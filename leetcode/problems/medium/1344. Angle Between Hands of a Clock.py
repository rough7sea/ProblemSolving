class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        minutes %= 60

        angl_m = 360 / 60 * minutes
        m_angl_m = angl_m / 360 * 30

        angl_h = 360 / 12 * hour + m_angl_m

        m = min(abs(angl_h - angl_m), abs(angl_m - angl_h))

        return min(m, abs(360 - m))


sol = Solution()
# print(sol.angleClock(12, 30))
# print(sol.angleClock(2, 4))
print(sol.angleClock(1, 57))
