# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # Reach node at postion left
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev = cur
            cur = cur.next

        # reverse the portion between left and right
        prev = None
        for i in range(right - left + 1):
            # need this because broke chain via reversal
            tmpNext = cur.next
            cur.next = prev 
            prev, cur = cur, tmpNext 

        # make ends of ll correct
        leftPrev.next.next = cur # cur is the node after right
        leftPrev.next = prev
        return dummy.next

            