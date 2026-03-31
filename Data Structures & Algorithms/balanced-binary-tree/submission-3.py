# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        res = True

        if root is None:
            return True



        def dfs(root):

            length = 1
            nonlocal res

            if not root:
                return 0
            else:
                left = dfs(root.left)
                right = dfs(root.right)

                length += max(left, right)
                print(root.val, left, right)

                if abs(left - right) > 1:
                    res = False
            
            return length
        
        dfs(root)
        return res

            
        
