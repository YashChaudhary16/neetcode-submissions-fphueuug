class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(candidates)
        result = set()

        path = []
        path_sum = 0

        def backtrack(index, path_sum):
            # print(index, path, path_sum)
            if path_sum == target:
                result.add(tuple(path.copy()))
                return 
            
            if path_sum >= target or index >= len(nums):
                return
        
            path.append(nums[index])
            backtrack(index + 1, path_sum + nums[index])

            path.pop()
            backtrack(index + 1, path_sum)
        
        backtrack(0, path_sum)
        
        res = []
        for element in result:
            res.append(list(element))
        
        return res


