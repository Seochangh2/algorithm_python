class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n<=1:
            return [0]
        graph = collections.defaultdict(list)
        number = n
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        outs=[]
        for i in range(n+1):
            if len(graph[i]) == 1:
                outs.append(i)
        
        while number > 2:
            number-=len(outs)
            new_outs = []
            for out in outs:
                nei = graph[out].pop()
                graph[nei].remove(out)
                if len(graph[nei])==1:
                    new_outs.append(nei)
            outs=new_outs
        
        return outs

        
        