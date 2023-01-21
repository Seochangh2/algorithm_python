import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

N,M,K,X = map(int,input().split())

graph = [[] for _ in range(N+1)]
result = []
distance = [INF] * (N+1)

for m in range(M):
  a , b= map(int,input().split())
  graph[a].append((b,1))

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
        if distance[d] == K:
          result.append(d)
        elif d in distance:
          result.remove(d)
        

dijkstar(X)
if result:
  result.sort()
  print(*result)
else:
  print(-1)
