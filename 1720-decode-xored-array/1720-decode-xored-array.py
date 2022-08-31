class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        out = [first]
        for i in encoded:
            out.append(out[-1]^i)
        return out
        