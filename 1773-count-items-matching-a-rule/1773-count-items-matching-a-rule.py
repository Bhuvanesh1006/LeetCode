class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        k = {"type":0,"color":1,"name":2}
        count = 0
        for i in items:
            if i[k[ruleKey]] == ruleValue:
                count += 1
        return count
        