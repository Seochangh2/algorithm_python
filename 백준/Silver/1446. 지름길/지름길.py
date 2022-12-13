N,D = map(int,input().split())
short = []
dist = [ i for i in range(D+1)]
for n in range(N):
    a,b,c =  map(int,input().split())
    short.append([a,b,c])
    
for i in range(D+1):
    dist[i] = min(dist[i],dist[i-1]+1)
    
    for start,end,cost in short:
        if i == start and end<=D and dist[i]+cost < dist[end]:
            dist[end] = dist[i]+cost
print(dist[D])

