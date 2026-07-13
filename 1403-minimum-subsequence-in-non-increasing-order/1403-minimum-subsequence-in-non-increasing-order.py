class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        nums.sort(reverse=True)

        ans = []
        curr = 0

        for num in nums:
            ans.append(num)
            curr += num

            if curr > total - curr:
                return ans