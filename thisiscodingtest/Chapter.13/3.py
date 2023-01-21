import collections
N,K = map(int,input().split())
graph = []
viru = []
for n in range(N):
    L = list(map(int,input().split()))
    graph.append(L)
    for i,l in enumerate(L):
      if l != 0:
        viru.append((l,n,i))
viru.sort()
virus = collections.deque(viru)
S,X,Y = map(int,input().split())
move = [(0,-1),(0,1),(1,0),(-1,0)]
for s in range(S):
    for t in range(len(virus)):
        v, x , y = virus.popleft()
        if graph[x][y] != 0 :
            for dx,dy in move:
                nx,ny = x+dx,y+dy
                if nx < 0 or nx >= N or ny <0 or ny>=N:
                    continue
                if graph[nx][ny]==0 :
                    virus.append((graph[x][y],nx,ny))
                    graph[nx][ny] = graph[x][y]


print(graph[X-1][Y-1])