# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        L = []
        node = head
        while node is not None:
            L.append(node.val)
            node = node.next
            
        while len(L) > 1:
            if L.pop(0) != L.pop():
                return False
            
        return True
        