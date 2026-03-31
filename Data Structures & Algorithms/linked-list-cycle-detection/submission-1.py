# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        index = 1001
        curr_head = head

        while head.next:
            curr_head.val = index
            if curr_head.next is None:
                return False
            if curr_head.next.val > 1000:
                return True
            curr_head = curr_head.next
            index += 1
        
        return False
        