class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for nums in numSet:
            if(nums-1) not in numSet:
               length = 0
               while(nums + length) in numSet:
                    length += 1
               longest = max(length, longest)
        return longest

