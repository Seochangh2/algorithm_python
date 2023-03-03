N = int(input())

nums = list(map(int,input().split()))
memory = [0]*(N+1)
#memory[0] = nums[0]
for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            memory[i] = max(memory[i],memory[j])
    memory[i] += nums[i]

print(max(memory))