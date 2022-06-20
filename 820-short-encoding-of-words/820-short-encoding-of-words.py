class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len,reverse=True) 
        out=''
        for i in words: 
            if i+'#' not in out:   
                out+=i+'#'
        return len(out)
        