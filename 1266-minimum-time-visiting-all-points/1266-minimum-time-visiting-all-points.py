class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        sum1=0
        for k in range(len(points)-1):
            sum1+= max(abs(points[k][0]-points[k+1][0]),abs(points[k][1]-points[k+1][1]))
        return sum1
        