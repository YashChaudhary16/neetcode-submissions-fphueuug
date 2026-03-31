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
        visited = set()

        def backtrack(index):

            print(index, path, visited)
            # base case - store the combination
            if len(path) == len(digits):
                result.append("".join(path.copy()))
                return
            # invalid case
            if index >= len(digits):
                return
            
            for element in digit_dict[digits[index]]:
                path.append(element)
                backtrack(index + 1)
                path.pop()
        
        backtrack(0)
        return result