class Solution:
    def replaceDigits(self, s: str) -> str:
        alpha="abcdefghijklmnopqrstuvwxyz"
        res=''
        for i in range(len(s)):
            if s[i] in alpha:
                j=alpha.index(s[i])
                res+=s[i]
                if i<len(s)-1:
                    k=int(s[i+1])
                    res+=alpha[j+k]
        return res