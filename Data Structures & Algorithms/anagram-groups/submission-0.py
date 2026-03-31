class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        res_dict = {}
        for string in strs:
            res_dict[''.join(sorted(string))] = res_dict.get(''.join(sorted(string)), []) + [string]

        return res_dict.values()

        