class Solution:
    def minimumSum(self, num: int) -> int:
        bhu = sorted(str(num))
        return int(bhu[0] + bhu[3]) + int(bhu[1] + bhu[2])