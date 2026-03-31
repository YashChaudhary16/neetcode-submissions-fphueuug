class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        res = 1
        current_streak = 1

        nums = sorted(set(nums))

        for i in range(1, len(nums)):
            
            if nums[i] == nums[i-1] + 1:
                current_streak += 1
            else:
                res = max(res, current_streak)
                current_streak = 1
        
        return max(current_streak, res)
