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
        dummy = ListNode(0, head)
        pre1, pre2 = getNode(dummy, k - 1), getNode(dummy, n - k)
        node1, node2 = pre1.next, pre2.next
        next1, next2 = node1.next, node2.next

        if node2 == next1:
            pre1.next = node2
            node2.next = node1
            node1.next = next2
        elif node1 == next2:
            pre2.next = node1
            node1.next = node2
            node2.next = next1
        else:
            pre1.next = node2
            node2.next = next1
            pre2.next = node1
            node1.next = next2
        
        return dummy.next
        