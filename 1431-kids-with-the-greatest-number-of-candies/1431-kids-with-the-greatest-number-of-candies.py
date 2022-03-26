class Solution:
    def kidsWithCandies(self, ca: List[int], ex: int) -> List[bool]:
        res=[]
        maxi=max(ca)
        for i in range(len(ca)):
                if ca[i]+ex>=maxi:
                    res.append(True)
                else:
                    res.append(False)
        return res
        
        