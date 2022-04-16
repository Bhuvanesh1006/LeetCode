class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n%2==0:
            return n-1
        else:
            return (((n-1)//2)*2)
            
        