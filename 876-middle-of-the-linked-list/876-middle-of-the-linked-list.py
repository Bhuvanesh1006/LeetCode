# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        h=head
        while h:
            count+=1
            h=h.next
        h=head
        mid=count//2
        for i in range(mid):
            h=h.next
        return h