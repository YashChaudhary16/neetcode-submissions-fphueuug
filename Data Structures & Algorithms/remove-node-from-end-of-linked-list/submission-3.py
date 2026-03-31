# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        res = head
        slow = head
        fast = head
        target_jump = n
        forward_index = True

        while fast:
            fast = slow
            while target_jump > 0:
                target_jump -= 1
                fast = fast.next
            if forward_index and fast is None:
                return head.next
            elif fast.next:
                slow = slow.next
                target_jump = n
                forward_index = False
                fast = slow
            else:
                slow.next = slow.next.next
                slow = slow.next
                break
        
        return res
