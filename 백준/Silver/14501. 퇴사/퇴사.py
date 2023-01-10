import collections
memory = collections.defaultdict(int)
N = int(input())
T=[]
P=[]
max_val = 0
for _ in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)

for i in range(N-1,-1,-1):
    time = T[i]+ i
    if time > N:
        memory[i] = max_val
    else:
        memory[i] = max(max_val,memory[time]+P[i])
        max_val = memory[i]

print(max_val)