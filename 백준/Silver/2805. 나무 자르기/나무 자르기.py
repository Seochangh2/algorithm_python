N,M = map(int,input().split())

trees = list(map(int,input().split()))
start, end = 0, max(trees)
result = 0
while start<=end:
    mid = (start+end) // 2
    tmp = 0
    for t in trees:
        if t > mid:
            tmp += t-mid
    if tmp < M :
        end = mid -1
    else :
        start = mid + 1
        result = mid

print(result)