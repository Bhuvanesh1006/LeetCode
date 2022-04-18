import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        st="abcdefghijklmnopqrstuvwxyz"
        for i in st:
            if i not in sentence.lower():
                return False
        return True
            