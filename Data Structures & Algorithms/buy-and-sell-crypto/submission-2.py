class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0
        
        max_profit = 0

        left = 0
        right = 1

        while right < len(prices):
            if prices[right] - prices[left] > 0:
                max_profit = max(max_profit, prices[right] - prices[left]) 
                right+=1
            else:
                left = right
                right += 1
        
        return max_profit
