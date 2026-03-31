class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        path = []

        def backtrack(index):

            # base case
            if index >= len(nums):
                result.append(path.copy())
                return result
            
            # condition 1 - include the element at curr index
            path.append(nums[index])
            backtrack(index + 1)

            # condition 2 - don't include the element at curr index
            path.pop()
            backtrack(index + 1)
        
        backtrack(0)

        return result



        