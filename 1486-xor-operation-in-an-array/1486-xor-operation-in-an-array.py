class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(0,n):
            ans ^= start+2*i
        return ans
            
        