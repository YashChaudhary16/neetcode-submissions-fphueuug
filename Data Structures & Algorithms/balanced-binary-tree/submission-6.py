# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        res = True

        def dfs(node):
            nonlocal res
            length = 1
            if not node:
                return 0
            
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                print(left, right)
                res = res and abs(left - right) <= 1

                length += max(left, right)

                return length
        
        dfs(root)

        return res
            
        
