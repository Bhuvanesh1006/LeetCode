class Solution(object):
    def maxProduct(self,s):
        out=0
        s.sort(reverse=True)
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if (s[i]-1)*(s[j]-1)>out:
                    out=(s[i]-1)*(s[j]-1)
        return out
                    
        