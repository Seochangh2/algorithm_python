import sys,math
sys.setrecursionlimit(10**6)
def solution():
    board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
    answer = sys.maxsize
    N = len(board)
    move=[(0,1),(0,-1),(1,0),(0,-1)]
    turn=[(-1,1),(1,1),(-1,-1),(1,1)]
    def dfs(start,end,cnt,turning):
        s1,s2 = start[0],start[1]
        e1,e2 = end[0],end[1]
        if (math.sqrt((s1 ** 2) + (s2 ** 2))) < (math.sqrt((e1 ** 2) + (e2 ** 2))) :
            s1,e1 = e1,s1
            s2,e2 = e2,s2

        if s1 < 0 or s1 >= N or s2 <0 or s2>=N or e1 < 0 or e1 >= N or e2 <0 or e2>=N:
            return sys.maxsize
        if board[s1][s2] == 1 or board[e1][e2] ==1 :
            return sys.maxsize
        if turning == 1:
            return 0
            
        if(s1==(N-1) and s2==(N-1)) or (e1==(N-1) and e2==(N-1)):
            answer = min(answer,cnt)
        for i in range(4):
            dx,dy = move[i]
            tx,ty = turn[i]
            sx,sy = s1+dx,s2+dy
            ex,ey = e1+dx,e2+dy           
            dfs((sx,sy),(ex,ey),cnt+1,0)
            if s1 == e1:
                if dfs((s1+tx,s2),(e1,e2),cnt,1) == 0:
                     dfs((s1+tx,s2+ty),(e1,e2),cnt+1,0)
            else :
                if dfs((s1,s2+ty),(e1,e2),cnt,1) == 0:
                     dfs((s1+tx,s2+ty),(e1,e2),cnt+1,0)
                        
        
        
    dfs((0,0),(0,1),0,0)
    print(answer)
solution()