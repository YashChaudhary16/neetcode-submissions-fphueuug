class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        res = {}

        for char in s:
            if char not in res:
                res[char] = 1
            else:
                res[char]+=1

        for char in t:
            if char in res and res[char]:
                res[char]-=1
            else:
                res[char]=1
        
        print(res)

        res_val = 0

        for val in res.values():
            res_val+=abs(val)

        return res_val == 0
        