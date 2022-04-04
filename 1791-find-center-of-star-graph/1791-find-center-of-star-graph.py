from collections import Counter
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        node1=edges[0][0]
        node2=edges[0][1]
        if edges[1][0]==node1 or edges[1][1]==node1:
            return node1
        else:
            return node2