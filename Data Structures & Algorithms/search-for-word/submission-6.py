class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path = []
        visited = set()

        def backtrack(row, col, index, visited):

            if index == len(word):
                return True
            
            if (row < 0 or col < 0 or
                row >= len(board) or col >= len(board[0]) or
                board[row][col] != word[index] or
                (row, col) in visited):
                return False
            
            visited.add((row, col))

            result = backtrack(row + 1, col, index + 1, visited) or backtrack(row - 1, col, index + 1, visited) or backtrack(row, col + 1, index + 1, visited) or backtrack(row, col - 1, index + 1, visited)  
            visited.discard((row, col)) 
            return result
 

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0, visited):
                        return True

        return False