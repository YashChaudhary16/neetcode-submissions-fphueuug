class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res_dict = {}

        for i in range(len(nums)):
            if target - nums[i] in res_dict:
                return [res_dict[target - nums[i]], i]
            res_dict[nums[i]] = i