# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        min_node = False
        res = {}
        num = 0

        def dfs(node):

            nonlocal num, res

            if not node:
                return 0
            else:
                dfs(node.left)
                num+=1
                print(num, node.val)
                res[num] = node.val
                dfs(node.right)
            
            return num
        
        dfs(root)
        return res[k]


            