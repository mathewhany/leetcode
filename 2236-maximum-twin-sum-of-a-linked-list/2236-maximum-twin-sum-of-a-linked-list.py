# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head, head
        pre = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = pre
            pre = slow
            slow = tmp
        
        cur1, cur2 = pre, slow
        best = 0
        while cur1 and cur2:
            best = max(best, cur1.val + cur2.val)
            cur1 = cur1.next
            cur2 = cur2.next
        
        return best