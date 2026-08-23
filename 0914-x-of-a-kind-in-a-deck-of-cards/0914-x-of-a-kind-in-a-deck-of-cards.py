from typing import List
from math import gcd
from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = Counter(deck)

        x = 0
        for count in counts.values():
            x = gcd(x, count)

        return x >= 2
