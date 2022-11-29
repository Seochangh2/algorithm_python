N,M = map(int,input().split())
graph = []

for n in range(N):
  graph.append(list(map(int,input())))

def dfs(x,y):
  if x<0 or x>=N or y<0 or y>=M :
    return False

  if graph[x][y] != 1:
    graph[x][y] = 1

    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

    return True
  
  return False
  
count = 0
for n in range(N):
  for m in range(M):
      checker = dfs(n,m)
      if checker:count+=1

print(count)