import sys
import collections
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N,M,C = map(int,input().split())
graph = [[] for _ in range(N+1)]
time = [INF]*(N)
for m in range(M):
  x,y,z=map(int,input().split())
  graph[x].append((y,z))


q = []

heapq.heappush(q,(0,C))
while q:
  t,node = heapq.heappop(q)
  if time[node-1] <= t:
    continue
  time[node-1] = t
  for d,c in graph[node]:
    heapq.heappush(q,(t+c,d))

