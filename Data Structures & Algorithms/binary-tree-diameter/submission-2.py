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
                diameter = max(diameter, dfs(node.right, length) + dfs(node.left, length))
                length += max(dfs(node.right, length), dfs(node.left, length))
                return length
            
        
        dfs(root, length)
        return diameter