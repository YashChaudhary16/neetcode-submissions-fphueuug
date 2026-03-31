class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_height = 0
        left, right = 0, len(heights) - 1

        while left < right:
            max_height = max(max_height, min(heights[left], heights[right])*(right-left))

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        
        return max_height

            