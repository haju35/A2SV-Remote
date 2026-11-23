from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def compare(a, b):
            x = a + b
            y = b + a
            if x > y:
                return -1
            elif x < y:
                return 1
            return 0

        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(compare))

        if nums[0] == "0":
            return "0"
        return "".join(nums)


        