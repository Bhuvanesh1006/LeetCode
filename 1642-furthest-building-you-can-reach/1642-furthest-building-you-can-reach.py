class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        i = 1
        h = []
        ans = 0
        
        while i<len(heights):
            
            dif = heights[i] - heights[i-1]
            
            if dif<=0:
                ans += 1
            
            elif len(h) < ladders:
                heapq.heappush(h,dif)
                ans += 1
                
            else:
                heapq.heappush(h,dif)
                ele = heapq.heappop(h)
                if bricks >= ele: 
                    bricks -= ele
                    ans += 1
                    
                else:
                    break
            i += 1 
        return ans
        