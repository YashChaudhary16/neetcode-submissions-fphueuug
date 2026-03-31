class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict_row = {}
        dict_col = {}

        dict_cube = {}

        for i in range(len(board[0])):
            dict_row[i] = set()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in dict_row[i]:
                    return False
                else:
                    dict_row[i].add(board[i][j])
        
        for i in range(len(board[0])):
            dict_col[i] = set()
            for j in range(len(board[0])):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in dict_col[i]:
                    return False
                else:
                    dict_col[i].add(board[j][i])

        k = 0

        for i in range(0, len(board[0]), 3):
            for j in range(0, len(board[0]), 3):
                dict_cube[k] = set()
        
                for column in board[i:i+3]:
                    for num in column[j:j+3]:
                        if num != "." and num in dict_cube[k]:
                            return False  
                        dict_cube[k].add(num)  
                k += 1

        return True