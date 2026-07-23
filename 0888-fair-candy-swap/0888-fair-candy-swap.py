class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumAlice = sum(aliceSizes)
        sumBob = sum(bobSizes)

        diff = (sumBob - sumAlice) // 2

        bobSet = set(bobSizes)

        for x in aliceSizes:
            if x + diff in bobSet:
                return [x, x + diff]