N , M = map(int,input().split())
x,y,d = map(int,input().split())

direction = [(-1,0),(0,1),(1,0),(0,-1)]
board = []
for n in range(N):
    board.append(list(map(int,input().split())))
result = 0
def check_around(x,y):
    check = False
    for i in range(4):
        cx,cy = x+direction[i][0],y+direction[i][1]
        if cx < 0 or cx >= N or cy < 0 or cy >=M:
            continue
        if board[cx][cy] == 0:
            return True
    return check
while True:
    if board[x][y] == 0:
        board[x][y] = 2
        result += 1
    elif check_around(x,y) == False:
        cx,cy = x-direction[d][0],y-direction[d][1]
        if board[cx][cy] == 1:
            break
        else :
            x,y = cx,cy
    elif check_around(x,y) == True:
        d = (d+3)%4
        cx,cy = x+direction[d][0],y+direction[d][1]
        if board[cx][cy] == 0:
            x,y = cx,cy
print(result)