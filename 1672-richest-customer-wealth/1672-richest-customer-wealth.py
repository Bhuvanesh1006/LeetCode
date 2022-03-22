class Solution:
    def maximumWealth(self, accounts):
        sum1 = []
        for i in accounts:
            sum1.append(sum(i))
        return max(sum1)