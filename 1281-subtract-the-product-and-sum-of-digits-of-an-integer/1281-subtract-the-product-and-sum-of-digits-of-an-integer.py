class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro=1
        su=0
        while n>0:
            k=n%10
            pro=pro*k
            su+=k
            n=n//10
        return pro-su