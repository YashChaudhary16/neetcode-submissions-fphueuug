import sys
sys.setrecursionlimit(100)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        open_brackets, close_brackets = n, n
        curr_path = []

        def backtrack(open_brackets, close_brackets):

            # base case - append it to the result, the valid solution
            if open_brackets == 0 and close_brackets == 0:
                result.append("".join(curr_path[:]))
                return result

            # invalid cases - such as ()())( or having more open/close brackets than "n"
            if close_brackets < open_brackets or open_brackets < 0 or close_brackets < 0:
                return
            
            # condition 1 - use open bracket
            curr_path.append("(")
            backtrack(open_brackets - 1, close_brackets)

            # condition 2 - use close bracket
            curr_path.pop()
            curr_path.append(")")
            backtrack(open_brackets, close_brackets - 1)
            curr_path.pop()
        
        backtrack(open_brackets, close_brackets)

        return result

        