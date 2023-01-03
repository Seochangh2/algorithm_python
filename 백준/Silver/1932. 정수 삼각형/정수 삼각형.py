
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
memory = [[0]*(i+1) for i in range(N)]
memory[0][0] = graph[0][0]
cumul = 0
for i,floor in enumerate(graph):
    J = len(floor)
    if i == 0:
        cumul += J
    else :
        for j in range(J):
            if j == 0:
                left = 0
            else :
                left = graph[i-1][j-1]
            if j == (J-1):
                right = 0
            else :
                right = graph[i-1][j]
            graph[i][j] = max(left,right) + graph[i][j]

print(max(graph[N-1]))