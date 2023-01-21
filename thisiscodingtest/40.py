import heapq
N,M = map(int,input().split())
INF = int(1e9)

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for m in range(M):
  a , b = map(int,input().split())
  graph[a].append((b,1))
  graph[b].append((a,1))

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
print(*distance)
min_num = 0
min_cost = INF
for n in range(2,N+1):
  if distance[n] > min_cost:
    min_num = n
    min_cost = distance[n]

print(min_num," ",min_cost," ",distance.count(min_cost))