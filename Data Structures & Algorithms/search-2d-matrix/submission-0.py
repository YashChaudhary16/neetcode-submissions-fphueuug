class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][left] == target:
                return True
            elif matrix[mid][right] == target:
                return True
            elif matrix[mid][left] > target:
                bottom = mid - 1
            elif matrix[mid][right] < target:
                top = mid + 1
            else:
                while left <= right:
                    mid_row = (left + right) // 2
                    if matrix[mid][mid_row] == target:
                        return True
                    elif matrix[mid][mid_row] < target:
                        left = mid_row + 1
                    elif matrix[mid][mid_row] > target:
                        right = mid_row - 1
            
        return False


        