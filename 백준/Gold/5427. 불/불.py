import copy,collections
T = int(input())
flag = 0
result = 1e9
directions = [(1,0),(0,-1),(0,1),(-1,0)]
R = []
def bfs(W,H,board,visited,q):
    while q:
        x,y = q.popleft()
        if visited[x][y] == "F":
            flag = "F"
        else:
            flag = visited[x][y]

        for dx,dy in directions:
            cx,cy = x+dx,y+dy
            
            if 0<=cx<H and 0<=cy<W:
                if visited[cx][cy] == -1 and (board[cx][cy] == '.' or board[cx][cy] == '@'):
                    if flag == "F":
                        visited[cx][cy] = flag
                    else:
                        visited[cx][cy] = flag+1
                    q.append((cx,cy))
            else:
                if flag != "F":
                    R.append(flag+1)
                    return
    R.append("IMPOSSIBLE")

for t in range(T):
    W,H = map(int,input().split())
    board = []
    visited = [[-1]*W for _ in range(H)]
    for h in range(H):
        board.append(list(input()))
    q = collections.deque()
    for i in range(H):
        for j in range(W):
            if board[i][j] == "@":
                visited[i][j] = 0
                start = (i,j)
            elif board[i][j] == "*":
                visited[i][j] = "F"
                q.append((i,j))
    q.append(start)
    bfs(W,H,board,visited,q)

for r in R:
    print(r)