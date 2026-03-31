# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        length = 1

        def dfs(node, length):
            if not node:
                return 0
            else:
                length += max(dfs(node.right, length), dfs(node.left, length))
                return length
        
        return dfs(root, length)
