class Solution:
    def minOperations(self, bo: str) -> List[int]:
        ans=[]
        for i in range(len(bo)):
            co=0
            for j in range(len(bo)):
                if i!=j:
                    if bo[j]=='1':
                        co+=abs(j-i)
            ans.append(co)
                    
        return ans
                    
                    
                
                