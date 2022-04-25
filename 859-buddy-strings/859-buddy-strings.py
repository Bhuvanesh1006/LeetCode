class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        l1 = list(s)
        l2 = list(goal)
        l = dict()
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                l[i] = l1[i]
        print(len(l))
        
        if len(l) > 2 or (len(l) < 2 and len(l) >0) :
            return False
        elif len(l) == 2:
            d = list(l.keys())
            l1[d[0]], l1[d[1]] = l1[d[1]], l1[d[0]]
            if l1 == l2:
                return True
        else:
            for i in l1:
                if l1.count(i) >= 2:
                    return True
            return False
        