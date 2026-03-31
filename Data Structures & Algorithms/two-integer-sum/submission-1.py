class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_dict = {}
        for i in range(len(nums)):
            if (target - nums[i]) not in difference_dict:
                difference_dict[nums[i]] = i
            else:
                return [difference_dict[target - nums[i]], i]
        return False