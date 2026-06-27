class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        i = 0
        n = len(s)

        # Skip spaces
        while i < n and s[i] == ' ':
            i += 1

        # Sign
        sign = 1
        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        # Build number
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign

        # Clamp
        if num < INT_MIN:
            return INT_MIN

        if num > INT_MAX:
            return INT_MAX

        return num