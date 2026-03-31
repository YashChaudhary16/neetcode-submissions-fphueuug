from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        level_dict = defaultdict(list)
        q = deque([(root, 0)])

        def bfs(node):
            nonlocal level_dict, q

            while q:
                curr = q.popleft()

                node = curr[0]
                level = curr[1]

                level_dict[level].append(node.val)

                if node.left:
                    q.append((node.left, level+1))
                if node.right:
                    q.append((node.right, level+1))

        bfs(root)

        res = [0]*len(level_dict)

        for key, value in level_dict.items():
            res[key] = value[-1]

        return res




