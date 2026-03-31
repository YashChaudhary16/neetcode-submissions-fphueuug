class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        left = 0  
        right = 0
        hash_check = dict()
        max_length = 0

        while right < len(s):
            if s[right] in hash_check:
                if hash_check[s[right]] < left:
                    hash_check[s[right]] = right
                    right += 1
                else:
                    left = hash_check[s[right]] + 1
                    hash_check[s[right]] = right
                    right += 1
            else:
                hash_check[s[right]] = right
                right += 1

            max_length = max(max_length, right - left)

        return max_length

        