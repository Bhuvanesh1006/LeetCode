class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and c == stack[-1][0]:
                if k-1 == stack[-1][1]: stack.pop()
                else: stack[-1] = [c, stack[-1][1]+1]
            else: stack.append([c, 1])
        return "".join(x*n for x,n in stack)
        