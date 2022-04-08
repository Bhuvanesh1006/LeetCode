class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0
        
        for ch in s:
            if ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
            else:
                continue
            max_depth = max(depth, max_depth)
        
        return max_depth
        