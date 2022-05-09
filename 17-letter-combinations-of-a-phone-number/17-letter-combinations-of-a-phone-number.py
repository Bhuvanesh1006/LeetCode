from collections import OrderedDict
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dis = { "2":'abc',  "3":'def',\
                     "4":'ghi',  "5":'jkl',\
                     "6":'mno',  "7":'pqrs',\
                     "8":'tuv',  "9":'wxyz'}
        output = [""]
        for d in digits:
            output = [i+j for i in output for j in dis[d]]
        if output == [""]:
            output = []
        return output
        