N = int(input())
M = int(input())
bus = [[int(1e9)]*(N+1) for _ in range(N+1)]
for n in range(1,N+1):
    bus[n][n] = 0
for m in range(M):
    a,b,c = map(int,input().split())
    if c < bus[a][b]:
        bus[a][b] = c

for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            bus[a][b] = min(bus[a][b],bus[a][k]+bus[k][b])        

for i in range(1,N+1):
    for j in range(1,N+1):
        if bus[i][j] >= int(1e9):
            print(0,end=" ")
        else:
            print(bus[i][j],end=" ")
    print()