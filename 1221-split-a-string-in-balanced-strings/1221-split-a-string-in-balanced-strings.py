class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countr,countl,ans=0,0,0
        for i in s:
            if i=="L":
                countl+=1
            else:
                countr+=1
            if countr==countl:
                ans+=1
        return ans