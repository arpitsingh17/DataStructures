# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(88)
        dummy.next = head
        varnode = dummy
        
        while varnode != None and varnode.next != None:
            if varnode.next.val == val:
                varnode.next = varnode.next.next
            else:
                varnode = varnode.next
        
        return dummy.next