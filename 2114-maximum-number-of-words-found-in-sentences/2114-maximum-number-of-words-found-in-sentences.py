class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi=0
        for k in sentences:
            if(len(k.split(" "))>maxi):
                maxi=len(k.split(" "))
        return maxi
                
        