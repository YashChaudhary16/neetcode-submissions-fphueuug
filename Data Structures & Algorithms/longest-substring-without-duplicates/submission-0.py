class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)
            
        right = 0
        hash_check = dict()
        max_length = 0

        while right < len(s):
            if s[right] in hash_check:
                right = hash_check[s[right]] + 1
                hash_check.clear()
                hash_check[s[right]] = right
                right+=1
            else:
                hash_check[s[right]] = right
                max_length = max(max_length, len(hash_check))
                right += 1

        return max_length

        