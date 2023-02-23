N = int(input())
result = 0
memory = [1]*10

for i in range(1,N):
    for j in range(8,-1,-1):
        memory[j] += memory[j+1]

print(sum(memory)%10007)