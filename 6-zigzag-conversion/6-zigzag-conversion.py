class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [''] * numRows
        cur, down = 0, 0

        for c in s:
            rows[cur] += c
            if cur == 0 or cur == numRows-1:
                down ^= 1
            cur += 1 if down else -1
        
        return ''.join([r for r in rows])
        
        