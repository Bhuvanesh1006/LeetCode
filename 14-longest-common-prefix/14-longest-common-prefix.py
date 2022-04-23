class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m=min(strs,key=len)  
        res=""
        for i,j in enumerate(m):
            for s in strs:
                if s[i]!=j:
                    return res
            res+=j
        return res