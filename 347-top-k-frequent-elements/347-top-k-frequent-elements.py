class Solution:
    def topKFrequent(self, nu: List[int], bhu: int) -> List[int]:
        return [x[0] for x in Counter(nu).most_common(bhu)]
        