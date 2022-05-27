class Solution(object):
    def numberOfSteps(self, num):
        st=0
        while num!=0:
            if num%2 == 0:
                num=num/2
                st+=1
            else:
                num-=1
                st+=1
        return st
                
        