class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        cnts = Counter(arr)
        vals = sorted([_ for _ in cnts])
        num_vals = len(vals)
        raw_sols = []
        for i in range(0, num_vals):
            val_i = vals[i]
            cnts[val_i] -= 1
            for j in range(i, num_vals):
                val_j = vals[j]
                val_k = target - val_i - val_j
                if val_k < val_j:
                    break
                if cnts[val_j] > 0:
                    cnts[val_j] -= 1
                    if cnts[val_k] > 0:  # and val_k >= val_j:
                        raw_sols.append((val_i, val_j, val_k))
                    cnts[val_j] += 1
            cnts[val_i] += 1
      
        result = 0
        for raw_sol in raw_sols:
            sol_cnts = Counter(raw_sol)
            total_ways = 1
            for val, cnt in sol_cnts.items():
                x = comb(cnts[val], cnt)
                total_ways *= x
            result += total_ways
            result %= 1000000007
            
        return result
