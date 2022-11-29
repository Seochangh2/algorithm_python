from collections import deque
N,M = map(int,input().split())
graph = []

for n in range(N):
  graph.append(list(map(int,input())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
q = deque()
q.append((0,0))
while q:
  x,y = q.popleft()
  
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if nx<0 or nx>=N or ny<0 or ny>=M :
      continue
    if graph[nx][ny] == 0:
      continue

    if graph[nx][ny] == 1:
      graph[nx][ny] = graph[x][y]+1
      q.append((nx,ny))

print(graph[N-1][M-1])