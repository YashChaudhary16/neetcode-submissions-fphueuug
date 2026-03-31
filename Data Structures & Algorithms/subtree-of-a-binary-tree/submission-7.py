# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        res = []

        def check_if_same(a, b):

            if not a and not b:
                return True
            
            elif not a or not b:
                return False
            
            if a.val == b.val:
                r = check_if_same(a.right, b.right)
                l = check_if_same(a.left, b.left)
            
            else:
                return False

            return l and r

        if root and subRoot and root.val == subRoot.val:
            if check_if_same(root, subRoot):
                return True

        if not root or not subRoot:
            return False
        
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)