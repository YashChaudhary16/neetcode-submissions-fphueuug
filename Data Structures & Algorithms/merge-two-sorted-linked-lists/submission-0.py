# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        curr_res = res
        A = list1
        B = list2

        while A and B:
            if A.val < B.val:
                curr_res.next = ListNode(A.val)
                curr_res = curr_res.next
                A = A.next
            else:
                new_node = ListNode(B.val)
                curr_res.next = ListNode(B.val)
                curr_res = curr_res.next
                B = B.next
        
        while A:
            new_node = ListNode(A.val)
            curr_res.next = ListNode(A.val)
            curr_res = curr_res.next
            A = A.next

        while B:
            new_node = ListNode(B.val)
            curr_res.next = ListNode(B.val)
            curr_res = curr_res.next
            B = B.next

        return res.next
