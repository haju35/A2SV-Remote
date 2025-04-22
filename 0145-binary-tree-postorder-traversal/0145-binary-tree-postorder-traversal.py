# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [(root, False)]  # Stack holds tuples of (node, visited_flag)
        res = []

        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    res.append(cur.val)
                else:
                    stack.append((cur, True))       # Add current node back with visited=True
                    stack.append((cur.right, False))  # Push right child
                    stack.append((cur.left, False))   # Push left child

        return res