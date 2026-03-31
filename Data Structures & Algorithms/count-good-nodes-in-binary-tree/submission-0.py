# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good_nodes = 0
        max_node = -101
        
        def dfs(node, max_node):
            nonlocal good_nodes

            if not node:
                return 0
            
            else:
                if node.val >= max_node:
                    good_nodes += 1

                max_node = max(max_node, node.val)

                dfs(node.left, max_node)
                dfs(node.right, max_node)
                
                return max_node
        
        dfs(root, max_node)

        return good_nodes

