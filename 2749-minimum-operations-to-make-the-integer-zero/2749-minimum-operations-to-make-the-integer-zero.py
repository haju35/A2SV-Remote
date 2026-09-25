class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            x = num1 - k * num2
            if x < k:
                continue
            if bin(x).count('1') <= k:
                return k
        return -1