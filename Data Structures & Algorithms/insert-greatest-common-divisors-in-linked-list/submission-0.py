# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # euclids alg for GCD!
        # A = 48 B = 18
            # 48 % 18 = 12
            # 18 % 12 = 6
            # 12 % 6 = 0 !!!
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a

        cur = head
        while cur.next:
            n1, n2 = cur.val, cur.next.val
            cur.next = ListNode(gcd(n1, n2), cur.next)
            cur = cur.next.next

        return head
