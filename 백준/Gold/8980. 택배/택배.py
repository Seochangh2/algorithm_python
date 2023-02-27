import sys
input = sys.stdin.readline

N,C = map(int,input().split())
M = int(input())
boxes = []
for m in range(M):
    a,b,c = map(int,input().split())
    boxes.append((a,b,c))
boxes.sort(key=lambda x :  x[1])
capacity = [C]*(N+1)
result = 0
for start,end,cost in boxes:
    min_c = C
    for i in range(start,end):
        if min_c > min(capacity[i],cost):
            min_c = min(capacity[i],cost)
    for i in range(start,end):
        capacity[i] -= min_c
    result += min_c
    
print(result)
    
    
    