N = int(input())
board = []
for n in range(N):
    board.append(list(input()))
if N == 1:
    print(board[0][0])
else:
        
    result = ""
    def sol(x,y,leng):
        global board
        
        if leng <= 1:
            return str(board[x][y])
        a = sol(x,y,leng//2)
        b = sol(x,y+leng//2,leng//2)
        c = sol(x+leng//2,y,leng//2)
        d = sol(x+leng//2,y+leng//2,leng//2)
        
        if a == b == c == d and len(a) == 1:
            return a
        else :
            return "("+a+b+c+d+")"

    result = sol(0,0,N)
    print(result)