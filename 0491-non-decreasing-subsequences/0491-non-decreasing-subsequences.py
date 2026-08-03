from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            if len(path) >= 2:
                result.append(path[:])

            used = set()

            for i in range(start, len(nums)):
                # Skip duplicates at the same recursion level
                if nums[i] in used:
                    continue

                # Ensure non-decreasing order
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return result