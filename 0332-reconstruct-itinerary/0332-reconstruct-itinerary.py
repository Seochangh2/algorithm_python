class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(start):
            
            while(mytickets[start]):
                end = mytickets[start].pop(0)
                dfs(end)
            route.append(start)

        
        mytickets = collections.defaultdict(list)
        route = []
        for ticket in sorted(tickets):
            mytickets[ticket[0]].append(ticket[1])

        dfs("JFK")
        return route[::-1]
    