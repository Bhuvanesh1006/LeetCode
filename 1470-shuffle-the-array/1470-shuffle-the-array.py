class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        bhu= []
        
        for i in range(n):
            bhu.append(nums[:n][i])
            bhu.append(nums[n:][i])
        
        return bhu
		
        
        
        