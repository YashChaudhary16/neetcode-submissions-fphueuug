class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        res_dict = {}

        def ascii_product(string):
            product = 1
            for character in string:
                product *= ord(character)
            return product


        for string in strs:
            res_dict[ascii_product(string)] = res_dict.get(ascii_product(string), []) + [string]

        return res_dict.values()
        