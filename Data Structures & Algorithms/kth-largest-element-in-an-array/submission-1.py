class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        total_length = len(nums)
        new_k = total_length - k + 1

        heapq.heapify(nums)
        res = 0

        while new_k > 0:
            res = heapq.heappop(nums)
            new_k -= 1
        
        return res
