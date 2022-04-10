class Solution:
    def calPoints(self, ops: List[str]) -> int:
        x=[]
        for i in range(len(ops)):
            if ops[i]=="+":
                x.append(x[-1]+x[-2])
            elif ops[i]=="D":
                x.append(2*x[-1])
            elif ops[i]=="C":
                x.pop()
            else:
                x.append(int(ops[i]))
        return sum(x)