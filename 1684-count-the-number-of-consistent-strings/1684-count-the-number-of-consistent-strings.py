class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        out=0
        for i in words:
            for j in set(i):
                if j not in allowed:
                    out+=1
                    break
                
        return len(words)-out