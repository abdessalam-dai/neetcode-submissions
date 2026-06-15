class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row_index
        u, b = 0, len(matrix) - 1

        row_index = matrix[0]
        while u <= b:
            row_index = (u + b) // 2

            if target < matrix[row_index][0]:
                b = row_index - 1
            elif target > matrix[row_index][-1]:
                u = row_index + 1
            else:
                break
        
        row = matrix[row_index]
        l, r = 0, len(row) - 1

        while l <= r:
            m = (l + r) // 2
            if target < row[m]:
                r = m - 1
            elif target > row[m]:
                l = m + 1
            else:
                return True
        
        return False
                