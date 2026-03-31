class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0
        pseudo_max = 0

        if len(nums) == 0:
            return res
        
        maximum = max(nums)
        minimum = min(nums)

        bucket = [0]*((maximum - minimum)+1)
        print(bucket)

        for num in nums:
            bucket[num - minimum] += 1

        for item in bucket:
            if item != 0:
                pseudo_max += 1
            else:
                pseudo_max = 0
            res = max(pseudo_max, res)

        print(bucket)
        return res