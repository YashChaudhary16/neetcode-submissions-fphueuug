class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        result = []

        path = []
        path_sum = 0

        def backtrack(index, path_sum):
            # print(index, path, path_sum)
            if path_sum == target:
                result.append(path.copy())
                return 
            
            if path_sum >= target or index >= len(nums):
                return
        
            path.append(nums[index])
            backtrack(index + 1, path_sum + nums[index])

            path.pop()
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index+=1
            backtrack(index + 1, path_sum)
        
        backtrack(0, path_sum)      
        return result


