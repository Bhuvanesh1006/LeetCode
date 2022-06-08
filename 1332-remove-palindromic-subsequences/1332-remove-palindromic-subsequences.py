class Solution(object):
    def removePalindromeSub(self, s):
        temp = s
        if(temp==s[::-1]):
            return 1
        else:
            return 2