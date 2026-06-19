class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lengths = [0] * n
        current_len = 0

        # Step 1: Forward pass to track lengths dynamically
        for i in range(n):
            char = s[i]
            if char.islower():
                current_len += 1
            elif char == '*':
                current_len = max(0, current_len - 1)
            elif char == '#':
                current_len *= 2
            elif char == '%':
                pass  # Length stays the same
            lengths[i] = current_len

        # If k is out of bounds of the final string length
        if k >= current_len or current_len == 0:
            return "."

        # Step 2: Backward pass to decode index k
        for i in range(n - 1, -1, -1):
            char = s[i]
            prev_len = lengths[i - 1] if i > 0 else 0

            # If k points to the character newly added in this step
            if char.islower() and k == lengths[i] - 1:
                return char

            if char == '#':
                # Undo duplication using modulus on the previous tracked length
                if k >= prev_len:
                    k %= prev_len

            elif char == '%':
                # Undo reversal by mirroring across the midpoint
                k = lengths[i] - 1 - k

            elif char == '*':
                # Characters removed at this step don't contain k
                # because k was validated to be within bounds of the final string.
                pass

        return "."
