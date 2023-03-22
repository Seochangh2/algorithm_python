N = int(input())
K = int(input())
start,end = 0,K

while start<=end:
    mid = (start+end)//2
    cnt = 0
    for i in range(1,N+1):
        cnt += min(N,mid//i)
    if cnt < K:
        start = mid +1
    else:
        result = mid
        end = mid -1
print(result)