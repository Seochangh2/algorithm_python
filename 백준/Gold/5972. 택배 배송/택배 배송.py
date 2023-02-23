import sys,heapq
N,M = map(int,input().split())
INF = sys.maxsize
graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)
for m in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstar(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        cost , node = heapq.heappop(q)
        if distance[node] < cost:
            continue
    
        for d , c in graph[node]:
            dist = cost + c
            if dist < distance[d]:
                distance[d] = dist
                heapq.heappush(q,(dist,d))
dijkstar(1)
print(distance[N])