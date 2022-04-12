class Solution:
    def minMovesToSeat(self, seats: List[int], stu: List[int]) -> int:
        seats.sort()
        stu.sort()
        c = 0
        for i in range(len(seats)):
            c += abs(stu[i] - seats[i])
        return c