import itertools,sys

N = int(input())
graph=[]
empty = []
teacher = []
result = "NO"
for n in range(N):
    L = list(input().split())
    graph.append(L)
    for m in range(N):
        if L[m] == "X":
            empty.append((n,m))
        if L[m] == "T":
            teacher.append((n,m))
            
combs = list(itertools.combinations(empty,3))

def DFS(x,y,graph,i):
    if x<0 or x>=N or y<0 or y>=N:
        return True
    if i == 0:
        while y>=0:
            if graph[x][y] == "S":
                return False
            if graph[x][y] == "O":
                return True
            y -= 1
    elif i == 1:
        while y<N:
            if graph[x][y] == "S":
                return False
            if graph[x][y] == "O":
                return True
            y += 1
    elif i == 2:
        while x>=0:
            if graph[x][y] == "S":
                return False
            if graph[x][y] == "O":
                return True
            x -= 1
    elif i == 3:
        while x<N:
            if graph[x][y] == "S":
                return False
            if graph[x][y] == "O":
                return True
            x += 1
    return True
def yes_or_no(graph):
    for t_x,t_y in teacher:
        for i in range(4):
            check = DFS(t_x,t_y,graph,i)
            if not check:
                return False
    return True
for comb in combs:
    a1,b1 = comb[0][0],comb[0][1]
    a2,b2 = comb[1][0],comb[1][1]
    a3,b3 = comb[2][0],comb[2][1]
    graph[a1][b1] = "O"
    graph[a2][b2] = "O"
    graph[a3][b3] = "O"
    
    if(yes_or_no(graph)):
        result ="YES"
        break
   
    graph[a1][b1] = "X"
    graph[a2][b2] = "X"
    graph[a3][b3] = "X"
    
print(result)