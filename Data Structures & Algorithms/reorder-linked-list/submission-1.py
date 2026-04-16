# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle using fast and slow ptr
        # split list in half
            # merge from from and back
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # second half
        second = slow.next
        slow.next = None
        prev = None
        # reverse second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge 2 halfs
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2