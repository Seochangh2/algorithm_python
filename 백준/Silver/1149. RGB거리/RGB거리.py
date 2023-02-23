N = int(input())

cost = []

for n in range(N):
    r,g,b = list(map(int,input().split()))
    cost.append([r,g,b])
    
result = 0
pre = 0
for n in range(1,N):
    cost[n][0] = min(cost[n-1][1],cost[n-1][2]) + cost[n][0]
    cost[n][1] = min(cost[n-1][0],cost[n-1][2]) + cost[n][1]
    cost[n][2] = min(cost[n-1][0],cost[n-1][1]) + cost[n][2]
print(min(cost[N-1]))