# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # base case
        if not root:
            return True

        diff = True
        length = 1

        def dfs(node, length):
            
            nonlocal diff

            if not node:
                return 0

            left = dfs(node.left, length)
            right = dfs(node.right, length)

            left += length
            right += length

            print(node.val, left, right)

            diff = diff and abs(left - right) <= 1

            return max(left, right)

        dfs(root, length)
        
        return diff


        