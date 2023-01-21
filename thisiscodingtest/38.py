N,M = map(int,input().split())

graph = [[int(1e9)]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
  graph[i][i] = 0

for m in range(M):
  a,b = map(int,input().split())
  graph[a][b] = 1

for k in range(1,N+1):
  for i in range(1,N+1):
    for j in range(1,N+1):
      graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

result = 0
for i in range(1,N+1):
  cnt = 0
  for j in range(1,N+1):
    if graph[i][j] != int(1e9) or graph[j][i] != int(1e9): cnt+=1
  if cnt == N : result +=1

for i in range(1,N+1):
    for j in range(1,N+1):
        if graph[i][j] >= int(1e9):
            print(0,end=" ")
        else:
            print(graph[i][j],end=" ")
    print()
print(result)
