# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result = root = ListNode(None)
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i,lists[i]))
        
        while heap :
            node = heapq.heappop(heap)
            
            index = node[1]
            result.next = node[2]
            
            result = result.next
            if result.next :
                heapq.heappush(heap,(result.next.val,index,result.next))
                
        return root.next