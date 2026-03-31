# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    
        length = 1
        diameter = 0

        def dfs(node, length):

            nonlocal diameter

            if not node:
                return 0
            else:
                left = dfs(node.left, length)
                right = dfs(node.right, length)
                diameter = max(diameter, left + right)
                length += max(left, right)
                return length
        
        dfs(root, length)
        return diameter