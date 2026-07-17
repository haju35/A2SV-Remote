class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        
        digits = [str(i) for i in range(1, n + 1)]
        result = []
        k -= 1  # convert to 0-indexed
        
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            idx = k // fact
            result.append(digits.pop(idx))
            k %= fact
        
        return ''.join(result)