import sys
graph = []
remain = [5]*5
for _ in range(10):
    graph.append(list(map(int,input().split())))

result = sys.maxsize
def sol(x,y,cnt):
    global result
    if x >= 10:
        sol(0,y+1,cnt)
    elif y >= 10:
        result = min(result,cnt)
    elif graph[x][y] == 1:
        for r in range(5):
            if remain[r] == 0:
                continue
            if x+r >= 10 or y+r >= 10:
                continue
            flag = 0
            for i in range(r+1):
                for j in range(r+1):
                    if graph[x+i][y+j] == 0:
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 0 :
                for i in range(r+1):
                    for j in range(r+1):
                        graph[x+i][y+j] = 0
                remain[r] -= 1        
                sol(x+i+1,y,cnt+1)
                remain[r] += 1
                for i in range(r+1):
                    for j in range(r+1):
                        graph[x+i][y+j] = 1
    else :
        sol(x+1,y,cnt)
sol(0,0,0)
print(result if result != sys.maxsize else -1 )