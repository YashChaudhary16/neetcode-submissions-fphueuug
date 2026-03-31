import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        left, right = -math.inf, math.inf
        res = True

        def dfs(node, left, right):
            if not node:
                return True
            
            if node.val <= left or node.val >= right:
                return False
            
            return dfs(node.right, node.val, right) and dfs(node.left, left, node.val)

        return dfs(root, left, right)