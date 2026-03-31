class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # sort the array - O(nlogn) time & O(n)
        nums = sorted(nums)

        result = []

        path = []
        path_sum = 0

        def backtrack(index, path_sum):

            # base case
            if path_sum == target:
                result.append(path.copy())
                return 
            # invalid case - no need to explore further
            if index >= len(nums) or path_sum > target:
                return 
            
            # use the current element
            path.append(nums[index])
            backtrack(index, path_sum + nums[index])

            # ignore the current element
            path.pop()
            backtrack(index + 1, path_sum)
        
        backtrack(0, path_sum)
        return result




            


