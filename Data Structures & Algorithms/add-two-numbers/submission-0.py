# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1r = None
        curr_l1 = l1
        l1_length = 0

        l2r = None
        curr_l2 = l2
        l2_length = 0

        while curr_l1:
            l1_length += 1
            new_node = ListNode(curr_l1.val)
            new_node.next = l1r
            l1r = new_node
            curr_l1 = curr_l1.next
        
        while curr_l2:
            l2_length += 1
            new_node = ListNode(curr_l2.val)
            new_node.next = l2r
            l2r = new_node
            curr_l2 = curr_l2.next
        
        l1r_iter = l1r
        l1r_str = ''
        while l1r_iter:
            l1r_str += str(l1r_iter.val)
            l1r_iter = l1r_iter.next

        l2r_iter = l2r
        l2r_str = ''
        while l2r_iter:
            l2r_str += str(l2r_iter.val)
            l2r_iter = l2r_iter.next

        res_int = str(int(l1r_str) + int(l2r_str))
        res_ll = ListNode()
        res_ll_dummy = res_ll
        for i in range(len(res_int)):
            res_ll_dummy.next = ListNode(int(res_int[i]))
            res_ll_dummy = res_ll_dummy.next

        res = None
        curr = res_ll.next

        while curr:
            new_node = ListNode(curr.val)
            new_node.next = res
            res = new_node
            curr = curr.next
        
        return res



                
        