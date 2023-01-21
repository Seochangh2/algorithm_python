import sys,itertools,collections,copy
N,M = map(int,input().split())
graph = []
result = -sys.maxsize
zero_list = []
for n in range(N):
    li = list(map(int,input().split()))
    graph.append(li)
    for m in range(M):
        if li[m] == 0:
            zero_list.append((n,m))
zero_comb = itertools.combinations(zero_list,3)
def dfs(map,x,y):
    if x<0 or x>=N or y<0 or y>=M:
        return
    if map[x][y] == 1 or map[x][y] == 3:
        return
    map[x][y] = 3
    dfs(map,x+1,y)
    dfs(map,x-1,y)
    dfs(map,x,y+1)
    dfs(map,x,y-1)
    
def find_safe(map,a,b,c):
    map[a[0]][a[1]] = 1
    map[b[0]][b[1]] = 1
    map[c[0]][c[1]] = 1
    for n in range(N):
        for m in range(M):
            if map[n][m] == 2:
                dfs(map,n,m)
    cnt = 0
    for n in range(N):
      cnt+= map[n].count(0)
    return cnt

for a,b,c in zero_comb:
    safe = find_safe(copy.deepcopy( graph),a,b,c)
    result = max(result,safe)

print(result)
        