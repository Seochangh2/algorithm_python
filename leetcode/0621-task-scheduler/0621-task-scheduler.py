class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = dict(collections.Counter(tasks))
        
        wait = collections.deque()
        
        remain = []
        time = 0
        for t in counter:
            heapq.heappush(remain,(-counter[t],t))
        
        while sum(counter.values()) != 0:
            if wait:
                w = wait.popleft()
                if w != "#":
                    heapq.heappush(remain,(-counter[w],w))
            if remain:
                now = heapq.heappop(remain)
                counter[now[1]] -= 1
                if counter[now[1]] > 0:
                    while len(wait)<n:
                        wait.append("#")
                    wait.append(now[1])

            time += 1
                    
        return time