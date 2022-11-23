class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append([v,w])
        
        Q = [(0,k)]
        dist = collections.defaultdict(int)

        while Q:
            time , node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v,w in graph[node]:
                    heapq.heappush(Q,(time + w , v))

        if len(dist) == n:
            return max(dist.values())

        return -1

