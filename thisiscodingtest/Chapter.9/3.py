import sys
import collections
import heapq
INF = sys.maxsize
input = sys.stdin.readline
N,M = map(int,input().split())
route = collections.defaultdict(list)

for m in range(M):
  a,b = map(int,input().split())
  route[a].append(b)
  route[b].append(a)

X,K = map(int,input().split())

distance_K = [INF]*(N+1)
distance_X = [INF]*(N+1)
def find_min(start,distance):
  q = []
  distance[start]=0
  heapq.heappush(q,(0,start))
  while q:
    count,node = heapq.heappop(q)
    if count > distance[node]:
      continue
    distance[node] = count
    for r in route[node]:
      heapq.heappush(q,(count+1,r))

find_min(1,distance_K)
find_min(K,distance_X)
if distance_K[K]+distance_X[X] < INF:
  print(distance_K[K]+distance_X[X])
else:
  print(-1)



