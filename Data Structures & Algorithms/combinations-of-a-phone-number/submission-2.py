class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []

        digit_dict = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        result = []
        path = []

        def backtrack(index):

            # base case - store the combination
            if len(path) == len(digits):
                result.append("".join(path.copy()))
                return

            # invalid case - index 
            if index >= len(digits):
                return
            
            # the core - for each element, you keep going deep until you reach an end
            # and then pop the last element to try another combination
            for element in digit_dict[digits[index]]:
                path.append(element)
                backtrack(index + 1)
                path.pop()
        
        backtrack(0)
        return result