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

def getNode(head, i):
    cur = head
    while i > 0:
        i -= 1
        cur = cur.next
    return cur
    

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = count(head)
        node1, node2 = getNode(head, k - 1), getNode(head, n - k)
        node1.val, node2.val = node2.val, node1.val

        return head
        