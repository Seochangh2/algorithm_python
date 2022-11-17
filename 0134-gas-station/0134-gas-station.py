class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # heap = []
        # save = 0
        # for i in range(len(cost)):
        #     heapq.heappush(heap,(-(gas[i]-cost[i]),i))
        # result = heap[0][1]
        # while heap:
        #     now = heapq.heappop(heap)
        #     idx=now[1]
        #     save += gas[idx]
        #     save -= cost[idx]
        #     if save<0:
        #         return -1

        if sum(gas) < sum(cost) :
            return -1

        result = save = 0
        for i in range(len(gas)):
            if save+gas[i] >= cost[i]:
                save += gas[i]-cost[i]
            else :
                result = i+1
                i = 0
                save = 0
        return result
        
        