# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if l1==None:
            return l2
        if l2==None:
            return l1
        cur=dum=ListNode()
        while l1 and l2:
            if l1.val>l2.val:
                cur.next=l2
                l2=l2.next
            else:
                cur.next=l1
                l1=l1.next
            cur=cur.next
            if l1 or l2:
                cur.next = l1 if l1 else l2
        return dum.next
        