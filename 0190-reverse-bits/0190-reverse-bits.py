class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = n & 1          # get the lowest bit of n
            result = (result << 1) | bit   # push it into result
            n >>= 1               # move to the next bit of n
        return result