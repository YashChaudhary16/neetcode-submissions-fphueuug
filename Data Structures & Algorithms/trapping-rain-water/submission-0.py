class Solution:
    def trap(self, height: List[int]) -> int:

        # in case of shortest height 
        if len(height) == 1:
            return 0

        
        left_highs = [height[0]] * len(height)
        right_highs = [height[-1]] * len(height)

        for i in range(1, len(height)):
            left_highs[i] = max(height[i], left_highs[i-1])
        
        for j in range(len(height) - 2, -1, -1):
            right_highs[j] = max(height[j], right_highs[j+1])

        trapped_water = 0
        
        for k in range(len(height)):
            if ((left_highs[k] > height[k]) and (right_highs[k] <= height[k])) or ((right_highs[k] > height[k]) and (left_highs[k] <= height[k])):
                continue
            else:
                if min(left_highs[k], right_highs[k]) > height[k]:
                    trapped_water += min(left_highs[k], right_highs[k]) - height[k]
                    
        return trapped_water
