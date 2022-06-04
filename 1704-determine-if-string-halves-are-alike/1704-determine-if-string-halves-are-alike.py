class Solution(object):
    def halvesAreAlike(self, s):
        vo=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O','U']
        ca=0
        cb=0
        a=s[:(len(s)/2)]
        b=s[len(s)/2:]
        for i in a:
            if i in vo:
                ca+=1
        for j in b:
            if j in vo:
                cb+=1
        if ca==cb:
            return True
        else:
            return False
            