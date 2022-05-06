class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j = ""
		
        for i in digits:
            j+=str(i)
			
        digits.clear() 
		
        k = int(j)+1
		
        for i in str(k):
            digits.append(int(i))
			
        return digits