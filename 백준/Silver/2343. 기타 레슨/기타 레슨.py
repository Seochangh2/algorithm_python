N,M = map(int,input().split())

classes = list(map(int,input().split()))

sum_c = sum(classes)

start = 0 
end = 1e9
result = sum_c

while start <= end:
    mid = (start+end) // 2
    if mid < max(classes):
        start = mid +1
        continue
    cnt,tmp = 0,0
    for i in range(len(classes)):
        if tmp+classes[i] <= mid:
            tmp += classes[i]
        else:
            tmp = classes[i]
            cnt += 1
    if cnt <= M-1:
        end = mid -1
        result = min(result,mid)
    else:
        start = mid + 1
        
print(int(result))