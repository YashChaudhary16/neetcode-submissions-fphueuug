class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res_t, res_s = {}, {}

        for char in t:
            if char in res_t:
                res_t[char] += 1
            else:
                res_t[char] = 1

        for chars in s:
            if chars in res_s:
                res_s[chars] += 1
            else:
                res_s[chars] = 1

        return res_s == res_t
