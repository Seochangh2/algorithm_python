# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        lst=[]
        while node:
            lst.append(node.val)
            node = node.next
        lst.sort()
        output = ListNode()
        result = output
        for num in lst:
            result.next = ListNode(num)
            result = result.next
        return output.next