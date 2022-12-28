import collections
N,L,R = map(int,input().split())
graph = []
move = [(1,0),(-1,0),(0,-1),(0,1)]
for n in range(N):
    lst = list(map(int,input().split()))
    graph.append(lst)
result = 0

def process(x,y,index,union):
    global graph,move,L,R
    united =[(x,y)]
    q = collections.deque()
    q.append((x,y))
    union[x][y] = index
    summary = graph[x][y]
    cnt = 1
    while q:
        a,b = q.popleft()
        for dx,dy in move:
            cx = a+dx
            cy = b+dy
            if cx <0 or cx>=N or cy<0 or cy>=N:
                continue
            sub = abs(graph[a][b]-graph[cx][cy])
            if L<= sub <=R and union[cx][cy]==-1:
                united.append((cx,cy))
                q.append((cx,cy))
                union[cx][cy] = index
                cnt += 1
                summary += graph[cx][cy]
    for i,j in united:
        graph[i][j] = summary//cnt
    return cnt
    
while True:
    union=[[-1]*N for _ in range(N)]
    idx = 0
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1:
                process(i,j,idx,union)
                idx += 1
    if idx ==(N*N):
        break
    result += 1

print(result)
            
