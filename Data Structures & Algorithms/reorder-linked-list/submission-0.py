# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # PART 1 - REVERSE THE LL
        length = 0
        reverse = None
        curr = head
        while curr:
            length += 1
            new_node = ListNode(curr.val)
            new_node.next = reverse
            reverse = new_node
            curr = curr.next

        # PART 2 - MERGE TWO LLs
        front = head
        backward = reverse

        iterator = 2

        while iterator < length:

            next_front = front.next
            next_backward = backward.next

            front.next = backward
            front = front.next 
            front.next = next_front
            front = front.next

            backward = next_backward
            iterator += 2
        
        if length % 2 == 1:
            front.next = None
        else:
            front.next = backward
            front = front.next
            front.next = None
