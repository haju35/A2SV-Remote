class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}

        # Find next greater element for every number in nums2
        for num in reversed(nums2):
            # Remove smaller elements
            while stack and stack[-1] <= num:
                stack.pop()

            # The top of stack is the next greater element
            if stack:
                next_greater[num] = stack[-1]
            else:
                next_greater[num] = -1

            # Add current number
            stack.append(num)

        # Get answers for nums1
        answer = []
        for num in nums1:
            answer.append(next_greater[num])

        return answer