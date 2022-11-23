# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def switch(pre,now):
            if not now :
                return pre
            else :
                nowNext = now.next
                out = switch(now,nowNext)
                now.next = pre
                return out
            
        if not head :
            return 
        
        headNext = head.next
        output = switch(head,headNext)
        head.next = None
            
        return output