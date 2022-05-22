class Solution(object):
    def countOperations(self, num1, num2):
        res=0
        while num1 and num2:
            if num1>=num2:
                num1-=num2
                res+=1
            else :
                num2-=num1
                res+=1
        return res
        