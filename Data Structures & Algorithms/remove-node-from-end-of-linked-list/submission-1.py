# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        res = head
        curr2 = head
        length = 0
        
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # base case
        if length == 1:
            return head.next

        forward_index = 1
        # other cases
        while curr2:
            if forward_index == 1 and length == n:
                return head.next
            else:
                length -= 1
                if length == n:
                    curr2.next = curr2.next.next
                    curr2 = curr2.next
                else:
                    curr2 = curr2.next
            forward_index += 1

        return res