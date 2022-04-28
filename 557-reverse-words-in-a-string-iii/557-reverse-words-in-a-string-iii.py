class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        return " ".join([s[i][::-1] for i in range(len(s))])