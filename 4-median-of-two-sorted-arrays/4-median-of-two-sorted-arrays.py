class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=sorted(nums1+nums2)
        k=len(a)
        if k%2 !=0:
            L=a[:(k//2)+1]
            return (L[-1])
        else:
            e1=a[:(k//2)]
            e2=a[(k//2):]
            return ((e1[-1]+e2[0])/2)
        