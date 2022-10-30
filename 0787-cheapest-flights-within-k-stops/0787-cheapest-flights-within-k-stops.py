class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        Q = [(0,src,k)]
        dist = collections.defaultdict(int)
        while Q:
            money , node , time = heapq.heappop(Q)
            
            if node == dst:
                return money
            if node not in dist or dist[node]<= time:
                dist[node] = time
                if time >= 0 :
                    for v,w in graph[node]:
                        heapq.heappush(Q,(money + w, v ,time-1))

        return -1