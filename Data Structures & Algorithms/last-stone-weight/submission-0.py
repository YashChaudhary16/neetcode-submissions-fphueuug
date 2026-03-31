class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        heapq._heapify_max(stones)

        while len(stones) > 1:

            x = heapq._heappop_max(stones)
            y = heapq._heappop_max(stones)

            if x != y:
                heapq._heappush_max(stones, x - y)
            
        stones.append(0)
        return stones[0]