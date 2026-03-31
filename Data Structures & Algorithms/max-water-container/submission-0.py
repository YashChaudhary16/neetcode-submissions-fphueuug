class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_height = 0

        for i in range(len(heights) - 1):
            for j in range(i+1, len(heights)):
                max_height = max(max_height, min(heights[i], heights[j])*(j-i))
        
        return max_height

            