# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head :
            return
        now = head
        root = ListNode()
        pre = root
        pre.next = head
        
        count = 1
        
        while now and now.next:
            if count % 2 == 1:
                tmp = now
                now = now.next
                pre.next , tmp.next  , now.next = now , now.next , tmp
                pre = now
                now = now.next
            else :
                pre = now
                now = now.next
            count +=1
                
        
        return root.next