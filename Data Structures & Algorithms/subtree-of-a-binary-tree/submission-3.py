# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False

        res = False

        def check_same(node, subnode):
            if not node and not subnode:
                return True
            if not (node and subnode) or (node.val != subnode.val):
                return False
            
            return check_same(node.left, subnode.left) and check_same(node.right, subnode.right)

        res = check_same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return res