# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Finds the lowest common ancestor (LCA) of two nodes p and q in a binary tree.
        
        This implementation follows the user's requested strategy:
        1. Find the path from the root to node p.
        2. Find the path from the root to node q.
        3. Store the nodes in p's path in a set for fast lookup.
        4. Iterate through q's path in reverse.
        5. The first node from q's path that is also in p's path set is the LCA.
        """

        path_p = []
        path_q = []

        self.findPath(root, p, path_p)

        self.findPath(root, q, path_q)

        path_p_set = set(path_p)
        
        for node in reversed(path_q):
            # 5. Check if the node is present in p's path
            if node in path_p_set:
                # 6. If a match is found, this is the LCA. Return it.
                return node

        return None

    def findPath(self, root: 'TreeNode', target: 'TreeNode', path: list) -> bool:
        if not root:
            return False

        path.append(root)
        
        if root.val == target.val:
            return True

        if self.findPath(root.left, target, path):
            return True

        if self.findPath(root.right, target, path):
            return True

        path.pop()
        
        return False