class Solution(object):
    def merge(self, nums1, m, nums2, n):
        Len = m + n
        while n > 0:
            nums1[Len-1] = nums2[n-1]
            n -= 1
            Len -= 1
        return nums1.sort()