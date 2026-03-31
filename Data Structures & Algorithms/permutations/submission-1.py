class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        visited = set()

        def backtrack():
            # Base Case: If the path is full, we've found a permutation
            if len(path) == len(nums):
                result.append(path[:]) # Create a copy of the path
                return

            # Recursive Step: Try every number in the list
            for i in range(len(nums)):
                num = nums[i]
                
                # If the number is already used in the current path, skip it
                if num in visited:
                    continue

                # 1. Action: Add the number to our path
                path.append(num)
                visited.add(num)

                # 2. Recurse: Move to the next position in the path
                backtrack()

                # 3. Backtrack: Undo the action to try the next number in the loop
                path.pop()
                visited.remove(num)

        backtrack()
        return result