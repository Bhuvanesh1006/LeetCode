class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        buckets = {}
        div = 1 if t==0 else t                              #necessary fix for the case where t = 0
            
        for i, x in enumerate(nums):
            if i > k:                                       #remove old elements from sliding window
                del(buckets[nums[i-k-1]//div])
            if x//div in buckets:                           #if bucket is occupied, return True
                return True
            if (x//div)-1 in buckets:                       #else check bucket immediately to the left
                if abs(x - buckets[(x//div)-1]) <= t:
                    return True
            if (x//div)+1 in buckets:                       #else check bucket immediately to the right
                if abs(x - buckets[(x//div)+1]) <= t:
                    return True
            buckets[x//div] = x    