# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        min_node = False
        res = 0
        num = 0

        def dfs(node, k):

            nonlocal num, res

            if not node:
                return 0
            else:
                dfs(node.left, k)
                num+=1
                if num == k:
                    res = node.val
                dfs(node.right, k)
            
            return num
        
        dfs(root, k)
        return res


            