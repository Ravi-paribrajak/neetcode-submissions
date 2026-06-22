class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = 0
        start_row = 0
        end_row = len(matrix) - 1
        end_col = len(matrix[target_row]) - 1
        while start_row <= end_row:
            mid = (start_row + end_row) // 2
            row_start = matrix[mid][0]
            row_end = matrix[mid][-1]
            if row_start <= target <= row_end:
                target_row = mid
                break
            elif row_start > target:
                end_row = mid - 1
            else: 
                start_row = mid + 1

        low = 0
        high = len(matrix[target_row]) - 1

        while low <= high:
            mid = (low + high) // 2
            item = matrix[target_row][mid]
            if item == target:
                return True
            elif item > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
