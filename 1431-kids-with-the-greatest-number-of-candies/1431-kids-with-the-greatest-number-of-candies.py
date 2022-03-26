class Solution:
    def kidsWithCandies(self, ca: List[int], ex: int) -> List[bool]:
        res=[]
        for i in range(len(ca)):
                if ca[i]+ex>=max(ca):
                    res.append(True)
                else:
                    res.append(False)
        return res
        
        