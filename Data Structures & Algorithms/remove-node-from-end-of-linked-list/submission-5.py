# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        slow = head
        fast = head
        jump = n + 1

        while jump > 0:
            if fast is None:
                return head.next
            fast = fast.next
            jump -= 1
        
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        slow = slow.next

        return head
