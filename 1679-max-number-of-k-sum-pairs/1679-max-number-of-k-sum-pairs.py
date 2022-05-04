class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        opr = 0
        num = {}
        for i in nums:
            num[i]= num.get(i, 0) + 1
        for i in nums:
            if num.get(i, 0) != 0 and num.get(k-i, 0) != 0:
                if k-i == i :
                    if num.get(i) > 1:
                        opr += 1
                        num[i] -= 2
                else:
                    opr += 1
                    num[i] -= 1
                    num[k-i] -= 1
        return opr