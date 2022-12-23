import collections
N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]

for k in range(K):
  x,y = map(int,input().split())
  board[x-1][y-1] = 2

L = int(input())
timer = collections.deque()
for l in range(L):
  X,C = input().split()
  timer.append((int(X),C))
dir = [(0,1),(1,0),(0,-1),(-1,0)]
sn_dir = 0
head = [0]*2
tail = collections.deque()
tail.append((0,0))
cnt = 0
while True:
  cnt += 1
  i,j = dir[sn_dir]
  head[0] += i
  head[1] += j
  x,y = head[0],head[1]
  print(x,"랑",y)
  if x < 0 or x >= N or y <0 or y>=N:
    break
  if board[x][y] == 1:
    print("여기")
    break
  if board[x][y] == 2:
    tail.append((x,y))
  elif board[x][y] == 0 :
    tail.append((x,y))
    i,j = tail.popleft()
    board[i][j] = 0
  board[x][y] = 1
  if timer :
    if timer[0][0] == cnt:
      print("s")
      X,C = timer.popleft()
    
      if C == "D":
        sn_dir = (sn_dir+1) % 4
      else :
        sn_dir -= 1
        if sn_dir < 0:
          sn_dir+=4

print(cnt)