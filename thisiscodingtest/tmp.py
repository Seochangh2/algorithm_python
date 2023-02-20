M, N, K = map(int,input().split())
graph = [[0]*M for _ in range(N)]
squares = []
for k in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for cx in range(x2-x1):
        for cy in range(y2-y1):
            graph[x1+cx][y1+cy] = 1
result = 0
widths = []
def dfs(x,y,graph):
    if x<0 or x>=N or y<0 or y>=M:
        return 0
    if graph[x][y] != 1:
        graph[x][y] = 1
        a = dfs(x+1,y,graph)
        b = dfs(x-1,y,graph)
        c = dfs(x,y+1,graph)
        d = dfs(x,y-1,graph)
        w = a+b+c+d+1
        return w
    return 0
    
    
print(graph)
for m in range(M):
    for n in range(N):
        if graph[n][m] == 0:
            widths.append(dfs(n,m,graph))
            result += 1
    
print(result)
widths.sort()  
print(*widths)