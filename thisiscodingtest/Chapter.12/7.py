import itertools,sys
N ,M = map(int,input().split())
graph = []
chicken = []
house =[]
for n in range(N):
    data = list(map(int,input().split()))
    graph.append(data)
    for i in range(N):
        if data[i] == 1:
            house.append((n,i))
        elif data[i] == 2:
            chicken.append((n,i))
def get_sum(combi):
    result = 0
    for hx,hy in house:
        tmp = sys.maxsize
        for cx,cy in combi:
            tmp = min(tmp,abs(hx-cx)+abs(hy-cy))
        result += tmp
    return result

combis = list(itertools.combinations(chicken,M))
min_leng = sys.maxsize
for combi in combis:
    min_leng = min(min_leng,get_sum(combi))

print(min_leng)