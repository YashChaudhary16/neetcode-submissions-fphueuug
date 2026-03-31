class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        hash_set = {}

        for num in nums:
            if num in hash_set:
                return num
            else:
                hash_set[num] = True