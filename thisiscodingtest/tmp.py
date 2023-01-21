N = int(input())
power = list(map(int,input().split()))

power.reverse()

result = [1]*N

for i in range(1,N):
    max_num = 0
    for j in range(i):
        if power[i] > power[j]:
            max_num = max(result[j]+1,max_num)
    result[i] = max_num
max_cnt = max(result)
print(result)
print(N," ",max_cnt)