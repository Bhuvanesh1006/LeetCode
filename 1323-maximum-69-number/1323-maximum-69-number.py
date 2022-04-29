class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        bool = True; 
        out =""

        for i in s:
            if(i == '6' and bool):               
                out = out + "9"
                bool = False
            else:
                out = out+i
            
    
        return int(out)