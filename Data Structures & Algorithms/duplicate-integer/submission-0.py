class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict = {}

        for num in nums:
            if num in mydict:
                return True
            else:
                mydict[num] = 1
        return False