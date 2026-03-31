import sys
sys.setrecursionlimit(100)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = set()
        path = []

        visited = set()

        def backtrack(index, visited):

            print(index, visited, path)
            if len(path) == len(nums):
                result.add(tuple(path.copy()))
                return result
            
            if index >= len(nums) or nums[index] in visited:
                return 
            
            path.append(nums[index])
            visited.add(nums[index])
            for i in range(len(nums)):
                backtrack(i, visited)

            path.pop()
            visited.discard(nums[index])
            backtrack(index + 1, visited)

        backtrack(0, visited)
        
        res = []

        for element in result:
            res.append(list(element))

        return res