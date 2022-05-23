class Solution(object):
    def maxProduct(self,s):
        s.sort(reverse=True)
        return (s[0]-1)*(s[1]-1)
                    
        