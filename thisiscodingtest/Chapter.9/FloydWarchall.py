import sys
input = sys.stdin.readline
INF = sys.maxsize

N , M = map(int,input().split())

graph = [[INF]*(N+1) for _ in range(N+1)]

for m in range(M):
  a , b, c = map(int,input().split())
  graph[a][b] = c

for n in range(1,N+1):
  graph[n][n] = 0

for k in range(1,N+1):
  for i in range(1,N+1):
    for j in range(1,N+1):
      graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for a in range(1,N+1):
  for b in range(1,N+1):
    if graph[a][b] == INF:
      print("INF",end=" ")
    else:
      print(graph[a][b],end=" ")
  print()