import sys
sys.setrecursionlimit(10**6)

T = int(input())
def dfs(graph,x,y):
    if x>=N or x<0 or y>=M or y<0:
        return
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(graph,x+1,y)
        dfs(graph,x-1,y)
        dfs(graph,x,y+1)
        dfs(graph,x,y-1)
        return True
    
for t in range(T):
    N,M,K = map(int,input().split())
    graph = [[0]*M for _ in range(N)]
    for k in range(K):
        a,b = map(int,input().split())
        graph[a][b] = 1
    cnt = 0
    for n in range(N):
        for m in range(M):
            check = dfs(graph,n,m)
            if check : cnt+=1
    print(cnt)


