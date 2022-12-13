import collections
N = int(input())
A , B = map(int,input().split())
M = int(input())

graph = [[] for _ in range(N+1)]
for m in range(M):
    p,c = map(int,input().split())
    graph[c].append(p)
    graph[p].append(c)

def bfs(root,target):
    q = collections.deque()
    q.append((root,0))
    visited = []
    while q:
        node,cnt = q.popleft()
        visited.append(node)
        if node == target:
            return cnt
        for g in graph[node]:
            if g not in visited:
                q.append((g,cnt+1))
    return -1

result = bfs(B,A)
print(result)