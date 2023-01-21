import heapq
N = int(input())
INF = int(1e9)
graph = []
for _ in range(N):
  l = list(map(int,input().split()))
  graph.append(l)

distance = [[INF] * (N) for _ in range(N)]
move = [(1,0),(-1,0),(0,1),(0,-1)]
def dijkstar(start_x,start_y):
  q = []
  distance[start_x][start_y] = 0
  heapq.heappush(q,(0,(start_x,start_y)))

  while q:
    cost , node = heapq.heappop(q)
    nx,ny = node

    if distance[nx][ny] < cost:
      continue
    for dx,dy in move:
      tx , ty = nx+dx,ny+dy
      if tx<0 or tx>=N or ty<0 or ty>=N:
        continue
      dist = cost + graph[tx][ty]
      if dist < distance[tx][ty]:
        distance[tx][ty]= dist
        heapq.heappush(q,(dist,(tx,ty)))

dijkstar(0,0)

for i in range(N):
  if distance[i] == INF:
    print("#")
  else:
    print(distance[i])
print(graph[0][0] + distance[N-1][N-1])