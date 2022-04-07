class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = sorted(stones,reverse = True)

        while(len(arr)>1):
            if arr[0]!=arr[1]:
                arr[0]-=arr[1]
                arr.pop(1)
                arr.sort(reverse=True)
            else:
                arr.pop(0)
                arr.pop(0)

        if(len(arr)==1):
            return arr[0]
        return 0
            
        