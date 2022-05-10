class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations = []
        curr = []
        pos = [i for i in range(1, 10)]
        
        def rec(idx, curr, curr_sum):
            if len(curr) == k and curr_sum == n:
                combinations.append(list(curr))
                return
            if len(curr) > k or curr_sum > n or idx >= 9: return
            x = pos[idx]
            # possibility 1: take the current item
            curr.append(x)
            rec(idx+1, curr, curr_sum+x)
            # possibility 2: dont take the current item
            curr.pop()
            rec(idx+1, curr, curr_sum)
        rec(0, [], 0)
        return combinations