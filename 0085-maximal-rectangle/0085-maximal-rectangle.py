class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        best = 0

        for row in matrix:
            # update histogram heights
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == "1" else 0

            # largest rectangle in histogram (sentinel 0 flushes the stack)
            stack = []  # indices with increasing heights
            for i in range(cols + 1):
                h = heights[i] if i < cols else 0
                while stack and heights[stack[-1]] >= h:
                    height = heights[stack.pop()]
                    left = stack[-1] if stack else -1
                    width = i - left - 1
                    best = max(best, height * width)
                stack.append(i)

        return best