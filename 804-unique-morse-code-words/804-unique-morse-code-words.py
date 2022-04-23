class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = "abcdefghijklmnopqrstuvwxyz"
        l = []
        ans = str()
        for i in words:
            for j in i:
                ans += morse[alpha.index(j)]
            l.append(ans)
            ans = str()
        return len(set(l))