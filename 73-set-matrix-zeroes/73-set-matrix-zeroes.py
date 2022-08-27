class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows = set()
        zero_columns = set()
        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_columns.add(j)
                    
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i in zero_rows or j in zero_columns:
                    matrix[i][j] = 0