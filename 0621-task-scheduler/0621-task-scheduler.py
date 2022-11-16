class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = dict(collections.Counter(tasks))
        can = []
        for t in counter:
            heapq.heappush(can,(-counter[t],t))

        wait = collections.deque()
        time = 0
        while sum(counter.values()) != 0 :
            if wait:
                w = wait.popleft()
                if w != "#":
                    heapq.heappush(can,(-counter[w],w))
            if can:
                t = heapq.heappop(can)
                counter[t[1]] -= 1
                if counter[t[1]] != 0 :
                    while len(wait) < n:
                        wait.append("#")
                    wait.append(t[1])

            time += 1

        return time
