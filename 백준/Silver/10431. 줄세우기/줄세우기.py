import bisect
for t in range(int(input())):
    l = list(map(int,input().split()))
    order = l[1:]
    peoples = [order[0]]
    cnt = 0
    for i in range(1,20):
        idx = bisect.bisect_left(peoples,order[i])
        peoples.insert(idx,order[i])
        cnt+=(i - idx)
    print(t+1,cnt)