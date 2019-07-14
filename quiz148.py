# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self,head):
        if not head or not head.next:
            return head
        pre=head
        slow=head
        fast=head
        while fast and fast.next:
            pre=slow
            slow=slow.next
            fast=fast.next.next
        left=head
        right=pre.next
        pre.next=None
        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge(left,right)
    
    def merge(self,left,right):
        pre=ListNode(-1)
        first=pre
        while left and right:
            if left.val<right.val:
                pre.next=left
                pre=left
                left=left.next
            else:
                pre.next=right
                pre=right
                right=right.next
        if left:
            pre.next=left
        else:
            pre.next=right
        return first.next
