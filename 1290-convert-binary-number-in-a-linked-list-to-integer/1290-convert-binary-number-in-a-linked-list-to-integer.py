# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        s=''
        while head:
            s+=str(head.val)
            head=head.next
        k=int(s)
        decimal,i,n=0,0,0
        while k!=0:
            dec=k%10
            decimal=decimal+dec * (2**i)
            k=k//10
            i+=1
        return decimal
            
        