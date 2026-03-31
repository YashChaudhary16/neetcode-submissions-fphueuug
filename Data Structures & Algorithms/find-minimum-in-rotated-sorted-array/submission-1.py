class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        while left < right:

            mid = ((left + right) // 2)

            if right - left == 1:
                return min(nums[left], nums[right])

            if nums[left] > nums[mid]:
                right = mid
            
            elif nums[mid] > nums[left]:
                if nums[left] > nums[right]:
                    left = mid + 1
                else:
                    right = mid

        return min(nums[left], nums[right])
        


