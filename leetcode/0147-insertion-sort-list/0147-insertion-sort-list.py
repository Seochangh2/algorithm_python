# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def other(self):
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

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = result = ListNode()

        while head:
            while cur.next and cur.next.val <= head.val :
                cur = cur.next
            
            cur.next ,head.next, head = head , cur.next ,head.next

            if head and cur.val > head.val:
                cur = result

        return result.next