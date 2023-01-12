N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
    
for i in range(1,N):
    J = len(graph[i])
    for j in range(J):
        if j == 0:
            left = 0
        else:
            left = graph[i-1][j-1]
        if j == J-1:
            right = 0
        else:
            right = graph[i-1][j]
        graph[i][j] += max(left,right)

print(max(graph[N-1]))