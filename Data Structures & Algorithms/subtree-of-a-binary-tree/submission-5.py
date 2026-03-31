# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def issametree(node1, node2):

            if not node1 and not node2:
                return True
            
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            return issametree(node1.left, node2.left) and issametree(node1.right, node2.right)

        res = False

        def dfs(node1, node2):

            nonlocal res

            if node1:

                if node1.val == node2.val:
                    res = res or issametree(node1, node2)
                
                dfs(node1.left, node2)
                dfs(node1.right, node2)
            
        dfs(root, subRoot)

        return res
                


