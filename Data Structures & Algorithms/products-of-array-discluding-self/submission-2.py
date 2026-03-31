from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        result = [1] * n

        # Build left product (inclusive of current element)
        left[0] = nums[0]
        for i in range(1, n):
            left[i] = left[i-1] * nums[i]

        # Build right product (inclusive of current element)
        right[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i]

        # Build result
        for i in range(n):
            if i == 0:                  # no left side
                result[i] = right[1]
            elif i == n-1:              # no right side
                result[i] = left[n-2]
            else:
                result[i] = left[i-1] * right[i+1]

        return result
