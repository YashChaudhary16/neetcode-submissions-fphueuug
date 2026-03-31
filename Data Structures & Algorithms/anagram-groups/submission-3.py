from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for string in strs:
            idx = 0
            mult = 1
            for char in string:
                idx += ord(char)
                mult *= ord(char)
            
            res[idx*mult].append(string)
        
        ans = []

        for value in res.values():
            ans.append(value)

        return ans