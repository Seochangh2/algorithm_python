# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        nums.sort()
        node = result
        for num in nums :
            result.next = ListNode(num)
            result = result.next

        
        return node.next

