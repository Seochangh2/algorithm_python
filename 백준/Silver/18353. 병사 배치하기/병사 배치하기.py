N = int(input())
power = list(map(int,input().split()))

power.reverse()

result = [1]*N

for i in range(1,N):
    max_num = 0
    for j in range(i):
        if power[i] > power[j]:
            result[i] = max(result[j]+1,result[i])
    
max_cnt = max(result)
print(N-max_cnt)