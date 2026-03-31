class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums_inv = [-num for num in nums]

        heapq.heapify(nums_inv)
        res = 0

        while k > 0:
            res = heapq.heappop(nums_inv)
            k-=1
        
        return -res
