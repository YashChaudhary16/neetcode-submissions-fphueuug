class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        res = []

        for [x, y] in points:
            heapq.heappush(heap, ((x - 0)**2 + (y - 0)**2, [x,y]))
        
        while k > 0:
            dist, point = heapq.heappop(heap)
            res.append(point)
            k-=1

        return res
