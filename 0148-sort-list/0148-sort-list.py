# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l1, l2):
            dummy = ListNode(0, None)
            prev = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next

                prev = prev.next
            
            prev.next = l1 if l1 else l2
            return dummy.next
        
        def split(l):
            dummy = ListNode(0, l)
            prev, slow, fast = dummy, l, l
            while fast and fast.next:
                prev, slow, fast = slow, slow.next, fast.next.next
            prev.next = None
            return dummy.next, slow
        
        def mergeSort(l):
            if not l or not l.next: return l

            l1, l2 = split(l)
            l1, l2 = mergeSort(l1), mergeSort(l2)

            return merge(l1, l2)
            
        
        return mergeSort(head)