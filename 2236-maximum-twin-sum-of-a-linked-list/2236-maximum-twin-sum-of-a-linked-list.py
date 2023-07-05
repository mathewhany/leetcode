# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        pre, cur = None, head
        while cur:
            pre = ListNode(cur.val, pre)
            cur = cur.next
        
        cur1, cur2= head, pre
        best = -inf
        while cur1 and cur2:
            best = max(best, cur1.val + cur2.val)
            cur1 = cur1.next
            cur2 = cur2.next
        return best