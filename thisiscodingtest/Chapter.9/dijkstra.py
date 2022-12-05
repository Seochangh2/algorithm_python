import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

N , M = map(int,input().split())
start = int(input())

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for m in range(M):
  a , b, c = map(int,input().split())
  graph[a].append((b,c))

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

dijkstar(start)
print(*distance)
for i in range(1,N+1):
  if distance[i] == INF:
    print("#")
  else:
    print(distance[i])

