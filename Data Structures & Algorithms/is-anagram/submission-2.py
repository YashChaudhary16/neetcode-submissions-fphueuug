class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dict = {}
        t_dict = {}

        for character in s:
            if character in s_dict:
                s_dict[character] += 1
            else:
                s_dict[character] = 1

        for character in t:
            if character in t_dict:
                t_dict[character] += 1
            else:
                t_dict[character] = 1    

        return s_dict == t_dict