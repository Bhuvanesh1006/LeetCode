class Solution:
    def isPalindrome(self, st1: str) -> bool:
        s = s = ''.join(ch for ch in st1 if ch.isalnum())        
        d=s.lower().lstrip()       
        n= len(d)
        if n==0 :
            return True
        for i in range (len(d)):
            return d==d[::-1]
        