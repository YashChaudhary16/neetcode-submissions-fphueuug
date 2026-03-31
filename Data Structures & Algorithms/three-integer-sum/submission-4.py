class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        resset = set()

        for i in range(len(nums)):
            left, right = i+1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + nums[i] == 0:
                    resset.add((nums[i], nums[left], nums[right]))
                    left+=1
                    right-=1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left+=1
                elif nums[left] + nums[right] + nums[i] > 0:
                    right-=1
        
        res = [list(item) for item in resset]

        return res
