# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head

        if s is None or s.next is None:
            return False

        f = s.next

        while f.next is not None and f.next.next is not None:
            if f.val == s.val:
                return True

            s = s.next
            f = f.next.next

        return False