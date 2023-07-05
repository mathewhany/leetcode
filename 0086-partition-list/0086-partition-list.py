# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummySmaller, dummyGreater = ListNode(), ListNode()
        prevSmaller, prevGreater = dummySmaller, dummyGreater
        cur = head
        while cur:
            next = cur.next
            cur.next = None

            if cur.val < x:
                prevSmaller.next = cur
                prevSmaller = prevSmaller.next
            else:
                prevGreater.next = cur
                prevGreater = prevGreater.next

            cur = next
        prevSmaller.next = dummyGreater.next
        return dummySmaller.next