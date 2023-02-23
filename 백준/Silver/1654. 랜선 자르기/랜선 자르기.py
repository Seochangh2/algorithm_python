K,N = map(int,input().split())

lan = []

for k in range(K):
    lan.append(int(input()))
    
start = 1
end = max(lan)
result = 0
while start<=end:
    mid = (start+end)//2

    cnt = 0
    for l in lan:
        c = l // mid
        cnt += c
    if cnt < N:
        end = mid - 1
    else :
        start = mid + 1

print(int(end))