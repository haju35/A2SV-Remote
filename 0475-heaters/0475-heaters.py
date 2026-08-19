from typing import List
from bisect import bisect_left

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()

        answer = 0

        for house in houses:
            i = bisect_left(heaters, house)

            # Distance to heater on the right
            right = float('inf')
            if i < len(heaters):
                right = heaters[i] - house

            # Distance to heater on the left
            left = float('inf')
            if i > 0:
                left = house - heaters[i - 1]

            # Closest heater for this house
            closest = min(left, right)

            # We need to cover the hardest-to-cover house
            answer = max(answer, closest)

        return answer
