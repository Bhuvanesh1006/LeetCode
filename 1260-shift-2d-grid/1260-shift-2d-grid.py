class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        a = len(grid)
        b = len(grid[0])
        dk = a*b
        bhu = [[0] * b for _ in range(a)]
        
        start = dk - k
        for i in range(a):
            for j in range(b):
                start %= dk
                r = start // b
                c = start % b
                bhu[i][j] = grid[r][c]
                start += 1
        return bhu
        