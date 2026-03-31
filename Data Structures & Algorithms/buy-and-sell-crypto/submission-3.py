class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        min_price = prices[0]
        minp = []
        for price in prices:
            min_price = min(min_price, price)
            minp.append(min_price)
        print(minp)

        max_price = prices[0]
        maxp = [prices[0]]
        for i in range(1, len(prices)):
            if minp[i] == minp[i-1]:
                max_price = max(max_price, prices[i])
                maxp.append(max_price)
            else:
                max_price = prices[i]
                maxp.append(prices[i])
        print(maxp)
        
        return max([x-y for x, y in zip(maxp, minp)])