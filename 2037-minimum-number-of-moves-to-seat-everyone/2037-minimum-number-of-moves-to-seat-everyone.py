from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        count = [0] * 101

        for seat in seats:
            count[seat] += 1

        for student in students:
            count[student] -= 1

        moves = 0
        unmatched = 0

        for i in range(101):
            unmatched += count[i]
            moves += abs(unmatched)

        return moves