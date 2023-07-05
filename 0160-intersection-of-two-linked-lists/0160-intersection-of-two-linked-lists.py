# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pre, cur = headB, headA
        while cur: 
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        slow, fast = pre, pre
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        ans = None
        if slow == fast:
            cur = pre
            while cur:
                if cur == slow:
                    ans = cur
                    break
                cur = cur.next
                slow = slow.next
        
        headA.next = None
        pre, cur = None, pre
        while cur: 
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return ans
        
