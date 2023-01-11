N = int(input())
memory = [1]*(N)
power = list(map(int,input().split()))

power.reverse()

for i in range(1,N):
    for j in range(0,i):
        if power[i] > power[j]:
            memory[i] = max(memory[i],memory[j]+1)
print(N-max(memory))