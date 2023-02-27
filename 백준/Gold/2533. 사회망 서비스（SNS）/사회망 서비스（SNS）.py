import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline 
N = int(input())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
dp = [[0,1] for _ in range(N+1)]
for i in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited[node] = True
    for n in graph[node]:
        if not visited[n]:
            dfs(n)
            dp[node][0] += dp[n][1]
            dp[node][1] += min(dp[n])
visited[1]  = True
dfs(1)

print(min(dp[1]))
