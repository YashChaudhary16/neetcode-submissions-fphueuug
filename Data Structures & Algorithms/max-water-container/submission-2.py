class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                max_area = max(min(heights[i], heights[j]) * (j - i), max_area)
        return max_area
        