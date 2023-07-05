# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = head

        while cur:
            prev = dummy
            while prev.next and prev.next.val < cur.val:
                prev = prev.next
            prevNext = prev.next
            curNext = cur.next
            prev.next = cur
            cur.next = prevNext
            cur = curNext
        
        return dummy.next
        
