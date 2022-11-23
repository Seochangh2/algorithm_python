class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        heap = []
        
        for p in people:
            heapq.heappush(heap,(-p[0],p[1]))
        
        result = []
        
        while heap:
            p = heapq.heappop(heap)
            result.insert(p[1],[-p[0],p[1]])
            
        return result
        