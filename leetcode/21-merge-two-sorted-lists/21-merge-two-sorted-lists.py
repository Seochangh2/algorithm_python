# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None and list2 is None:
            return 
        elif list1 is None and list2 is not None:
            return list2
        elif list1 is not None and list2 is None:
            return list1
        output = ListNode()
        head = output
        count = 0 
        while list1 is not None and list2 is not None:
            
            if  list1.val <= list2.val:
                output.val = list1.val
                output.next = ListNode()
                output = output.next
                list1 = list1.next
            elif list1.val > list2.val:
                output.val = list2.val
                output.next = ListNode()
                output = output.next
                list2 = list2.next
            if list1 is None:
                while list2 is not None:
                    output.val = list2.val
                    list2 = list2.next
                    if list2 is not None:
                        output.next = ListNode()
                        output = output.next
                        
            if list2 is None:
                while list1 is not None:
                    output.val = list1.val
                    list1 = list1.next
                    if list1 is not None:
                        output.next = ListNode()
                        output = output.next
            

        
        return head