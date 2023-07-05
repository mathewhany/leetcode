# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def count(head):
    count = 0
    cur = head
    while cur:
        count += 1
        cur = cur.next
    return count
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
            
        n = count(head)
        k %= n

        cur1, cur2 = head, head
        for _ in range(k):
            cur1 = cur1.next
        while cur1.next:
            cur2 = cur2.next
            cur1 = cur1.next
        cur1.next = head
        start = cur2.next
        cur2.next = None

        return start