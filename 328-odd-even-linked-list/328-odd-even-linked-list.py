# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        count = 1
        now = head
        tail = ListNode()
        head_t = tail
        while now and now.next :
            now.next , tail.next = now.next.next , now.next
            tail.next.next = None
            if now.next :
                now = now.next
            tail = tail.next
            
            
        now.next = head_t.next
        
        return head