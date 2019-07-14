# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        L,r=None,None
        p,q=l1,l2
        while p and q:
            if p.val<q.val:
                s=p
                p=p.next
            else:
                s=q
                q=q.next
            if not L:
                L=r=s
            else:
                r.next=s
                r=s
        if p:
            r.next=p
        if q:
            r.next=q
        return L
