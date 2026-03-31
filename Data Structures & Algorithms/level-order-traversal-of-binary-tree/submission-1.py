from collections import deque, defaultdict
from typing import Optional, List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # 1. The Dictionary of Lists (Your storage)
        # Using defaultdict(list) automatically creates a new list if the key doesn't exist
        levels_dict = defaultdict(list)
        
        # 2. The Queue (Your traversal mechanism)
        # We store TUPLES: (Node, Level Index)
        queue = deque([ (root, 0) ]) 

        while queue:
            # Pop the node AND its level
            curr, level = queue.popleft()
            
            # Add current value to the dictionary at the correct key
            levels_dict[level].append(curr.val)

            # Add children to the queue with "key + 1" (level + 1)
            if curr.left:
                queue.append((curr.left, level + 1))
            if curr.right:
                queue.append((curr.right, level + 1))

        # 3. Traverse dict and return as a list of lists
        # Since keys are 0, 1, 2... we can just iterate by range
        return [levels_dict[i] for i in range(len(levels_dict))]